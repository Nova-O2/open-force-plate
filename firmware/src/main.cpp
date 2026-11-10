// Open Force Plate — S2 bring-up (issue #2)
//
// Proof of life for the ESP32-S3 <-> ADS1256 SPI link:
//   1. reset the ADS1256 and read the STATUS register (chip ID must be 3);
//   2. configure one differential channel (AIN0/AIN1, PGA 64, 1000 SPS);
//   3. print raw 24-bit readings over USB serial.
// Press on the load cell wired to AIN0/AIN1: the value must move and come back.
//
// Pin map: docs/DEVELOPMENT_PLAN.md §1.3. Datasheet: TI ADS1256 (SBAS288).

#include <Arduino.h>
#include <SPI.h>

namespace pins {
constexpr int kSclk = 12;
constexpr int kMosi = 11;  // ADS1256 DIN
constexpr int kMiso = 13;  // ADS1256 DOUT
constexpr int kCs = 10;
constexpr int kDrdy = 9;
constexpr int kReset = 8;  // optional; leave the module's RESET high if unused
}  // namespace pins

namespace ads {
// Commands
constexpr uint8_t kWakeup = 0x00;
constexpr uint8_t kRdata = 0x01;
constexpr uint8_t kSdatac = 0x0F;
constexpr uint8_t kRreg = 0x10;
constexpr uint8_t kWreg = 0x50;
constexpr uint8_t kSelfcal = 0xF0;
constexpr uint8_t kSync = 0xFC;
constexpr uint8_t kReset = 0xFE;
// Registers
constexpr uint8_t kStatus = 0x00;
constexpr uint8_t kMux = 0x01;
constexpr uint8_t kAdcon = 0x02;
constexpr uint8_t kDrate = 0x03;
// Values
constexpr uint8_t kStatusAcalBufen = 0x06;  // auto-calibration on, input buffer on
constexpr uint8_t kMuxAin0Ain1 = 0x01;      // AINP = AIN0, AINN = AIN1
constexpr uint8_t kAdconPga64 = 0x06;       // clock out off, sensor detect off, PGA 64
constexpr uint8_t kDrate1000 = 0xA1;        // 1000 SPS (single channel, S2 only)
constexpr uint8_t kExpectedId = 3;
}  // namespace ads

// CLKIN = 7.68 MHz -> SCLK must stay below CLKIN/4 (1.92 MHz).
const SPISettings kSpi(1000000, MSBFIRST, SPI_MODE1);

// t6: 50 CLKIN periods between a read command and the first data bit (~6.5 us).
void waitT6() { delayMicroseconds(8); }

bool waitDrdy(uint32_t timeout_ms) {
  const uint32_t start = millis();
  while (digitalRead(pins::kDrdy) == HIGH) {
    if (millis() - start > timeout_ms) return false;
  }
  return true;
}

void sendCommand(uint8_t command) {
  SPI.beginTransaction(kSpi);
  digitalWrite(pins::kCs, LOW);
  SPI.transfer(command);
  digitalWrite(pins::kCs, HIGH);
  SPI.endTransaction();
}

uint8_t readRegister(uint8_t reg) {
  SPI.beginTransaction(kSpi);
  digitalWrite(pins::kCs, LOW);
  SPI.transfer(ads::kRreg | reg);
  SPI.transfer(0x00);  // read 1 register
  waitT6();
  const uint8_t value = SPI.transfer(0xFF);
  digitalWrite(pins::kCs, HIGH);
  SPI.endTransaction();
  return value;
}

void writeRegister(uint8_t reg, uint8_t value) {
  SPI.beginTransaction(kSpi);
  digitalWrite(pins::kCs, LOW);
  SPI.transfer(ads::kWreg | reg);
  SPI.transfer(0x00);  // write 1 register
  SPI.transfer(value);
  digitalWrite(pins::kCs, HIGH);
  SPI.endTransaction();
}

int32_t readData() {
  SPI.beginTransaction(kSpi);
  digitalWrite(pins::kCs, LOW);
  SPI.transfer(ads::kRdata);
  waitT6();
  uint32_t raw = static_cast<uint32_t>(SPI.transfer(0xFF)) << 16;
  raw |= static_cast<uint32_t>(SPI.transfer(0xFF)) << 8;
  raw |= SPI.transfer(0xFF);
  digitalWrite(pins::kCs, HIGH);
  SPI.endTransaction();
  if (raw & 0x800000) raw |= 0xFF000000;  // sign-extend 24 -> 32 bits
  return static_cast<int32_t>(raw);
}

bool initAds1256() {
  digitalWrite(pins::kReset, LOW);
  delay(1);
  digitalWrite(pins::kReset, HIGH);
  delay(5);
  sendCommand(ads::kReset);
  if (!waitDrdy(500)) return false;
  sendCommand(ads::kSdatac);

  const uint8_t status = readRegister(ads::kStatus);
  const uint8_t id = status >> 4;
  Serial.printf("STATUS = 0x%02X -> chip ID %u (expected %u)\n", status, id, ads::kExpectedId);
  if (id != ads::kExpectedId) return false;

  writeRegister(ads::kStatus, ads::kStatusAcalBufen);
  writeRegister(ads::kMux, ads::kMuxAin0Ain1);
  writeRegister(ads::kAdcon, ads::kAdconPga64);
  writeRegister(ads::kDrate, ads::kDrate1000);
  sendCommand(ads::kSelfcal);
  if (!waitDrdy(1000)) return false;

  Serial.printf("MUX = 0x%02X, ADCON = 0x%02X, DRATE = 0x%02X\n", readRegister(ads::kMux),
                readRegister(ads::kAdcon), readRegister(ads::kDrate));
  return true;
}

bool g_ready = false;

void setup() {
  Serial.begin(115200);
  delay(2000);  // give the USB CDC port time to enumerate

  pinMode(pins::kCs, OUTPUT);
  digitalWrite(pins::kCs, HIGH);
  pinMode(pins::kReset, OUTPUT);
  digitalWrite(pins::kReset, HIGH);
  pinMode(pins::kDrdy, INPUT);
  SPI.begin(pins::kSclk, pins::kMiso, pins::kMosi, pins::kCs);

  Serial.println("Open Force Plate — S2 SPI bring-up");
  g_ready = initAds1256();
  if (!g_ready) {
    Serial.println("ADS1256 not responding: check DVDD (3.3 V), wiring and pin map.");
    return;
  }
  sendCommand(ads::kSync);
  sendCommand(ads::kWakeup);
}

void loop() {
  if (!g_ready) {
    delay(1000);
    return;
  }
  static uint32_t last_print = 0;
  if (!waitDrdy(100)) {
    Serial.println("DRDY timeout");
    return;
  }
  const int32_t raw = readData();
  if (millis() - last_print >= 100) {  // 10 lines/s is enough to watch by eye
    last_print = millis();
    Serial.printf("raw=%ld\n", static_cast<long>(raw));
  }
}
