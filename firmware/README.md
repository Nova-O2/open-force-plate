# Firmware

ESP32-S3-DevKitC-1 N16R8 + ADS1256, built with [PlatformIO](https://platformio.org/) (Arduino framework). Pin map: [`docs/DEVELOPMENT_PLAN.md`](../docs/DEVELOPMENT_PLAN.md) §1.3.

**Current stage:** S2 SPI bring-up (#2) — reads the ADS1256 chip ID, configures AIN0/AIN1 at PGA 64 / 1000 SPS and prints raw values.

## Build

```bash
cd firmware
pio run
```

Without a local PlatformIO install, a disposable container works (the toolchain is cached in a Docker volume):

```bash
docker run --rm -v platformio-cache:/root/.platformio -v "$PWD":/fw -w /fw \
  python:3.12-slim sh -c 'pip install -q platformio==6.1.16 && pio run'
```

## Flash and watch

Plug the board through the port marked **USB** (native USB; serial output goes there), then:

```bash
pio run -t upload
pio device monitor
```

If the upload does not start, hold **BOOT**, tap **RESET**, release **BOOT**, and retry.

## Expected output (S2)

```
Open Force Plate — S2 SPI bring-up
STATUS = 0x30 -> chip ID 3 (expected 3)
MUX = 0x01, ADCON = 0x06, DRATE = 0xA1
raw=...
```

The STATUS low nibble may differ (it reflects ORDER/ACAL/BUFEN and DRDY); the chip ID is the high nibble. Pressing the cell on AIN0/AIN1 must move `raw` and release must bring it back. If the ID is wrong or DRDY times out: check the module DVDD (3.3 V), the five SPI wires and the pin map.
