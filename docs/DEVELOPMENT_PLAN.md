# Development Plan — Force Plate MVP

Single platform, uniaxial (Fz), 1000 Hz, USB-C + BLE, with Python analysis software.

---

## Phase 1: Hardware (Weeks 1–3)

### 1.1 Component Procurement

See [COMPONENTS_SELECTED.md](./COMPONENTS_SELECTED.md) for the complete purchase log (items, vendors, prices).

### 1.2 Mechanical Assembly

#### Top plate — 600 × 500 mm, aluminum 5052-F, 6.35mm (1/4in), rounded corners R30

- [ ] Source from local metal shop (with R30 rounded corners)
- [ ] Mark the positions of the 8 holes per the coordinate table (see below)
- [ ] Drill 8 holes of **Ø11 mm** (M10 clearance)
- [ ] Countersink holes at 90° to **Ø20 mm** (DIN 7991 M10, depth ~5.5 mm)
- [ ] Deburr holes with a metal file

#### Bottom plate — 527 × 396 mm, aluminum 3 mm, 15×15 chamfers at 45°

Single piece that covers the load cell mounting holes. Does not touch the floor — it is suspended between the cells and the nuts. The foot bolts sit outside the bottom plate area. Corners are chamfered to ensure they do not obstruct the cell threads.

- [ ] Source from local metal shop (together with the top plate, with 15×15 chamfers at all 4 corners)
- [ ] Drill 8 holes of **Ø11 mm** at the same relative positions as the top plate
- [ ] The bottom plate is centered under the top plate

:::tip Dual-plate strategy (Phase 5)
The top plate (50×60 cm) is sized to be cut in half → 2 plates of 50×30 cm (similar dimension to VALD FDLite: 48.5×30 cm). The Phase 1 holes are already at the correct angle (~62°) for the final Phase 2 layout.
:::

#### Load cell — Dimensions (Decent DYX-301 500 kg)

300 kg–1000 kg–2 ton range from the manufacturer's table:

| Dim | Value | Description |
|:---:|:-----:|-------------|
| A | 30 mm | Total length |
| B | 15 mm | Cable exit |
| C | **25 mm** | **Distance between mounting holes** |
| D | 76 mm | Total body |
| E | 30 mm | Width |
| W | 32 mm | Base width |
| H | 32 mm | Height |
| M | **M12 × 1.75** | **Foot bolt thread** |
| 2-Ø | **Ø13 mm** | **Cell hole diameter** (plate holes: Ø11 mm for M10) |
| I | 56 mm | Base length (bearing surface) |

#### Steel shims (4 units — 1 per cell)

Spacer between the cell and the top plate. Exact size of the cell base.

| Parameter | Value |
|-----------|-------|
| Material | Carbon steel or stainless steel |
| Thickness | 2 mm |
| Dimensions | **56 × 32 mm** (= cell base, dims I × W) |
| Holes | 2× Ø11 mm, 25 mm center-to-center |

**Function:** Distribute load and prevent the cell from digging into the aluminum (steel > aluminum in hardness). Do not use rubber — it dampens the signal at 1000 Hz.

#### Fastening — Assembly per cell

```
Allen bolt M10×50 DIN 7991 (flat countersunk head)
        ↓
[TOP plate — aluminum 6.35mm (1/4in), 600×500mm, R30]  ← Ø11mm hole countersunk Ø20 (5.5mm depth)
        ↓
[Shim — steel 2mm, 56×32mm]                             ← Ø11mm hole
        ↓
[DYX-301 cell — at ~62°]                                ← Ø13mm hole (cell)
        ↓
[BOTTOM plate — aluminum 3mm, 527×396mm]                ← Ø11mm hole
        ↓
M10 nut + washer
        ↓
[Foot bolt M12×1.75 with collar]  ← threaded into cell, outside bottom plate, rests on floor
```

**Fasteners required:** 8× M10×50 DIN 7991 + 8× M10 nuts + 8× washers (2 per cell)

#### Cell layout — ~62° (Phase 2 diagonal angle)

Cells oriented along the diagonal of the half-plate (300×500 mm), foot at the corner, cable toward the center. Angle already set for Phase 2 (cut in half).

```
    ←──────────── 600 mm ────────────→
    ┌────────────────┬────────────────┐ ↑
    │  foot          │          foot  │ │
    │    ╲C1         │        C2╱     │ │
    │      ╲         │        ╱       │ │
    │                │                │ 500mm
    │      ╱         │        ╲       │ │
    │    ╱C3         │        C4╲     │ │
    │  foot          │          foot  │ │
    └────────────────┴────────────────┘ ↓
                   CUT
```

#### Hole coordinates (origin: bottom-left corner)

| Cell | Point | X (mm) | Y (mm) |
|:----:|:-----:|:------:|:------:|
| C1 | Foot | 40.0 | 460.0 |
| C1 | Hole 1 | 56.7 | 428.1 |
| C1 | Hole 2 | 68.3 | 406.0 |
| C2 | Foot | 560.0 | 460.0 |
| C2 | Hole 1 | 543.3 | 428.1 |
| C2 | Hole 2 | 531.7 | 406.0 |
| C3 | Foot | 40.0 | 40.0 |
| C3 | Hole 1 | 56.7 | 71.9 |
| C3 | Hole 2 | 68.3 | 94.0 |
| C4 | Foot | 560.0 | 40.0 |
| C4 | Hole 1 | 543.3 | 71.9 |
| C4 | Hole 2 | 531.7 | 94.0 |

All plate holes: **Ø11 mm** (M10 clearance). Top plate: countersunk at 90° to Ø20 mm (DIN 7991). Same relative positions on bottom plate.

**Fabrication drawings:** regenerate via `python3 cad/fabrication_drawings.py` → 5 PDFs in `cad/` (plates, foot bolt, shim, assembly)

#### Turned foot bolt with collar (×4) — single machined part

| Part | Dimension |
|------|:---------:|
| Thread | M12×1.75, Ø12mm, **32 mm** length (= cell height) |
| Collar | **Ø20mm, 5 mm** height (stop — rests against cell) |
| Chamfer | Ø20→Ø60, 6 mm height (~17°) |
| Base | Ø60mm, **8 mm** thickness |
| Rubber pad | Ø60mm, 1 mm neoprene (glued after machining) |
| Material | Carbon steel or stainless steel (Ø60mm bar stock) |
| Total height | **52 mm** (thread + collar + chamfer + base + rubber) |

**No lock nut.** The collar acts as a mechanical stop — prevents the foot from threading beyond the cell height and reinforces the thread/chamfer transition. Height adjusted by threading. Platform weight locks position.

**Fabrication:** order from a machinist. Drawing: `hardware/cad/fab_foot_piece.pdf`

#### Mechanical assembly checklist

- [ ] Source top plate aluminum 5052-F, 600×500 mm, 6.35mm (1/4in), R30 corners
- [ ] Source bottom plate aluminum, 527×396 mm, 3 mm, 15×15 chamfers
- [ ] Source/fabricate 4 steel shims 56×32 mm, 2 mm (2× Ø11, 25 mm center-to-center)
- [ ] Order 4 turned foot bolts with collar (see specs above + `hardware/cad/fab_foot_piece.pdf`)
- [ ] Source Allen bolts M10×50 DIN 7991 (flat head) + M10 nuts + washers (8+8+8)
- [ ] Source Ø11 mm drill bit + 90° countersink for M10 (Ø20)
- [ ] Cut/source 4 rubber discs Ø60mm × 1mm (neoprene)
- [ ] Drill 8 holes Ø11 mm in plates (2 per corner, 25 mm spacing)
- [ ] Countersink the 8 holes in the top plate (Ø20, 90°, 5.5 mm depth)
- [ ] Deburr holes
- [ ] Glue rubber to foot bolts
- [ ] Assemble: DIN 7991 bolt → top plate (countersunk) → shim → cell → bottom plate → M10 nut + washer
- [ ] Thread foot bolts into cells (until collar contacts)
- [ ] Set on rigid, flat floor
- [ ] Level (adjust foot bolts by threading) — use bubble level
- [ ] Test rigidity — platform must not deflect under load

#### Structural reinforcement — Box section (2 square tubes)

The 6.35mm (1/4in) top plate alone deflects ~21 mm under drop jump load (120 kg, 5×BW) — unacceptable for a force platform. The solution is a **box section**: the two plates (top and bottom) act as flanges of a beam, connected by 2 aluminum square tubes bonded with structural epoxy.

| Parameter | Value |
|-----------|-------|
| Tube | Aluminum square 30×30 or 35×35×2 mm (subject to availability) |
| Quantity | 2 tubes, ~527 mm each (= bottom plate length) |
| Position | Longitudinal (X-axis), at Y=194 mm and Y=306 mm from top plate |
| Bonding | Structural epoxy (Araldite Professional or equivalent) |
| Shims | If tube < gap between plates, use aluminum shims to match height |

**Result:** I increases from 9,000 mm⁴ (plate alone) to ~1,060,000 mm⁴ (118× stiffer). Deflection drops from 21 mm to **<0.2 mm** across all scenarios.

```
Cross-section view (box section):
╔══════════════════════════╗  ← top plate 6.35mm (1/4in) (flange)
║    ┌────┐        ┌────┐  ║
║    │tube│        │tube│  ║  ← 2 bonded tubes (web)
║    │ 1  │        │ 2  │  ║     ~35mm height
║    └────┘        └────┘  ║
╚══════════════════════════╝  ← bottom plate 3mm (flange)
```

**Tube assembly:**

- [ ] Assemble one corner (1 cell + bolts + plates) to measure the actual gap between plates
- [ ] Source 2 aluminum square tubes (~527 mm each). Ideal size: measured gap ±1 mm
- [ ] If tube is smaller than gap: fabricate shims (thin aluminum strips cut to 35×527 mm)
- [ ] Sand bonding faces (80-grit, matte surfaces)
- [ ] Degrease with isopropyl alcohol
- [ ] Apply structural epoxy to all 4 bonding faces (top and bottom of each tube)
- [ ] Position tubes at Y=194 mm and Y=306 mm (ref. top plate), parallel to long axis
- [ ] Clamp for 24 h (epoxy cure)
- [ ] Verify alignment and flatness after cure

:::info Complete structural analysis
Calculation scripts in `cad/structural_analysis.py`, `cad/material_comparison.py`, `cad/reinforcement_analysis.py`, and `cad/box_section_analysis.py`. Deflection and stress verified for scenarios up to DJ 7×BW (120 kg), with FS > 10 in all cases.
:::

:::warning
Rigid, flat floor required. Uneven surfaces, carpet, or flexible floors compromise readings. If the floor is inadequate, use an MDF or plywood base as a leveling surface.
:::

### 1.3 Electronics Assembly

#### Power architecture

```
                          ┌──► ESP32 DevKit (5V pin → onboard reg → 3.3V)
USB-C 5V ──► TP4056 ──┐  │
              │        ├──┤
         Battery 3.7V ─┘  │
              │            └──► ADS1256 (AVDD 5V)
              ▼
         MT3608 (3.7V→5V) ──► same 5V bus
                                    │
                               [On/off button] ──► bus
```

**USB-C mode (primary):** 5V direct from USB powers everything. MT3608 inactive.
**Battery mode (BLE):** MT3608 converts 3.7V→5V. Everything works without a cable.

**⚠️ MT3608 — BEFORE FIRST USE:** Turn the blue trimpot ~20 turns counterclockwise to start at low output voltage. Connect a multimeter to VOUT+/VOUT− and turn slowly clockwise until reading **5.0V**. Only then connect to the circuit. High output can damage the ESP32 or ADS1256.

#### Signal diagram

```
Cell 1 (E+,E-,S+,S-)──┐                                    ┌──► BLE ──► PC/App
Cell 2 (E+,E-,S+,S-)──┼──► ADS1256 ──SPI──► ESP32-S3 ──────┤
Cell 3 (E+,E-,S+,S-)──┤     (24-bit)        (firmware)      └──► USB-C ──► PC/App
Cell 4 (E+,E-,S+,S-)──┘     1000 Hz
```

**Configuration:** 4 differential channels (1 per cell). PGA=64 (range ±78 mV).

#### SPI connections (ADS1256 → ESP32-S3)

| ADS1256 | ESP32 GPIO |
|---------|:----------:|
| SCLK | 18 |
| MOSI (DIN) | 23 |
| MISO (DOUT) | 19 |
| CS | 5 |
| DRDY | 4 |

#### Electronics assembly checklist

- [ ] Assemble power circuit on breadboard (TP4056 → MT3608 → 5V bus)
- [ ] Adjust MT3608 to 5.0V (use multimeter!)
- [ ] Connect on/off button between MT3608 and bus
- [ ] Connect ESP32-S3 to breadboard (5V pin + GND)
- [ ] Connect ADS1256 to breadboard (AVDD 5V + GND)
- [ ] Connect ADS1256 to ESP32-S3 via SPI (5 wires — see table above)
- [ ] Solder/connect 4 load cells to ADS1256 (E+, E−, S+, S− per cell)
- [ ] Connect EPB 1S2P battery to TP4056 (B+, B−) — **adapt connector JST-XH-2P → JST-PH 2.0mm** (use PH kit already purchased)
- [ ] Connect resistor voltage divider (2× 100kΩ) from battery B+ to ESP32 GPIO34 (voltage monitoring)
- [ ] Connect 3 battery indicator LEDs (green/yellow/red) to GPIOs 21/22/25
- [ ] Connect on/off button with integrated LED (already indicates "power on")
- [ ] Test power in both modes (USB-C and battery)
- [ ] **Measure actual battery capacity** (EPB 1S2P 5200 mAh, honest density 432 Wh/L) — controlled discharge 4.2V→3.0V with logger/coulomb counter
- [ ] Validate readings from all 4 cells (raw value on serial monitor)
- [ ] Validate battery voltage reading (compare ADC vs multimeter)

#### Battery Management — charging and monitoring

**Charging:**

| Parameter | Value |
|-----------|:-----:|
| Input | USB-C 5V (TP4056) |
| Charge current | 1000 mA |
| Charge time 0→100% | ~5.2 h (5200 mAh / 1000 mA) |
| Auto cutoff | 4.2 V ± 1% |
| Charge rate | C/5 (safe) |
| BMS protection | dual (TP4056 + internal pack BMS) |

**TP4056 LEDs (on-board, visible through case opening):**
- Red: charging
- Green: charge complete

**4-layer monitoring:**

**1. Voltage reading via ESP32 ADC (GPIO34)**

```
Battery B+ (up to 4.2V)
      │
      ├─[ R1 = 100kΩ ]──┬──► ESP32 GPIO34 (ADC)
      │                 │
      ├─[ R2 = 100kΩ ]──┤
      │                 │
     GND ──────────────┘
```

2:1 divider protects ADC (3.3V max). Software multiplies reading by 2.

**2. Voltage → SoC (State of Charge) — Li-ion 1S lookup table**

| Voltage | SoC | Status |
|:-------:|:---:|--------|
| 4.20 V | 100% | Full |
| 4.00 V | ~85% | — |
| 3.80 V | ~60% | — |
| 3.70 V | ~40% | Medium |
| 3.60 V | ~20% | Warning |
| 3.40 V | ~10% | Critical |
| 3.00 V | 0% | BMS cuts off |

**3. Indicator LEDs on case (GPIO driven)**

| LED | GPIO | Behavior |
|-----|:----:|---------|
| Green | 21 | SoC > 50% — solid on |
| Yellow | 22 | SoC 20–50% — solid on |
| Red | 25 | SoC < 20% — slow blink (1 Hz) |
| Red | 25 | SoC < 10% — fast blink (4 Hz) |

**4. Exposed via BLE/USB-C**

- BLE: Battery Service (UUID 0x180F) + Battery Level Characteristic (UUID 0x2A19) — value 0–100%
- USB-C: `battery` field included in the data stream to the app
- App shows icon + percentage in the interface

### 1.4 Theoretical System Resolution

```
4× DYX-301 500 kg = 2000 kg total = 19,620 N full scale
Sensitivity: 2.0 mV/V × 5V = 10 mV full scale per cell
ADS1256 PGA=64: range ±78 mV
Effective bits at 1000 Hz: ~17-18 bits

Per channel (500 kg / 4,905 N):
  17 eff bits: 4,905 / 131,072 = 0.037 N
  18 eff bits: 4,905 / 262,144 = 0.019 N

Combined (2000 kg / 19,620 N):
  17 eff bits: ~0.15 N
  18 eff bits: ~0.075 N

VALD FDLite comparison: ~0.15 N → we match or exceed
```

---

## Phase 2: Firmware (Weeks 2–4)

### 2.1 Environment Setup

- [ ] Install PlatformIO (VS Code or CLI)
- [ ] Create ESP32-S3 project with Arduino framework
- [ ] Add ADS1256 library (or implement SPI driver)

### 2.2 Data Acquisition

- [ ] Implement continuous ADS1256 reading at 1000 Hz
- [ ] Validate actual rate with oscilloscope or sample counter
- [ ] Implement circular buffer to smooth jitter
- [ ] Add timestamp (microseconds) to each sample

### 2.3 USB-C + BLE Communication

- [ ] Implement USB CDC (serial) on ESP32-S3 via native USB-C
  - Primary mode: USB-C for maximum reliability and throughput
  - Serial protocol: same packets as BLE
- [ ] Implement BLE GATT server on ESP32
  - Secondary mode: BLE for wireless use (portability)
- [ ] Define characteristics (BLE) / commands (USB):
  - `force_data` (notify/stream) — real-time data stream
  - `sample_rate` (read/write) — configure rate
  - `tare` (write) — zero the platform
  - `calibration` (read/write) — calibration factor
  - `battery` (read, notify) — battery level 0–100% (BLE: Battery Service 0x180F, Battery Level Char 0x2A19)
- [ ] Packet protocol: [timestamp_us(4B) | force_raw(4B) | force_N(4B)]
- [ ] Auto-detection: if USB-C connected → use USB; else → BLE
- [ ] Test BLE throughput — 1000 Hz × 12 bytes = 12 KB/s (within BLE limit)
- [ ] Test USB-C throughput — no practical limitation at 1000 Hz

### 2.4 Calibration

- [ ] Implement tare routine (zero with empty platform)
- [ ] Implement calibration with known weight:
  1. Empty platform → record zero
  2. Known weight (e.g. 20 kg) → record reading
  3. Calculate factor: `force_N = (raw - zero) × (weight_kg × 9.81) / (raw_weight - zero)`
- [ ] Save calibration to ESP32 EEPROM/NVS
- [ ] Implement multi-point calibration (0, 20, 40, 60, 80 kg) for linearity

---

## Phase 3: Software — Python App (Weeks 3–6)

### 3.1 BLE Acquisition

- [ ] Use `bleak` (Python) to connect to ESP32
- [ ] Implement BLE stream reception in a separate thread
- [ ] Data buffer with timestamps
- [ ] CSV logging: `timestamp_us, force_raw, force_N`

### 3.2 Real-Time Visualization

- [ ] Dashboard with `matplotlib` or `pyqtgraph` (faster):
  - Force × time plot (rolling window)
  - Current force (N and kg)
  - Peak indicator
  - BLE connection status
- [ ] Web alternative: Streamlit or FastAPI + WebSocket + Chart.js

### 3.3 Jump Analysis

Use/adapt the `force-plate-jump-analyses` package or implement:

- [ ] **Automatic phase detection:**
  1. Quiet standing
  2. Eccentric phase (unweighting)
  3. Concentric phase (propulsion)
  4. Flight
  5. Landing

- [ ] **CMJ/SJ metrics:**
  - Jump height (impulse-momentum and flight time methods)
  - Peak force (N and N/kg)
  - Rate of force development (RFD) — peak and mean
  - Net impulse (N·s)
  - Time to peak force (ms)
  - Mean power (W and W/kg)
  - Takeoff velocity (m/s)

- [ ] **DJ metrics:**
  - RSI (reactive strength index) = jump height / contact time
  - Modified RSI = jump height / total contraction time
  - Contact time (ms)
  - Flight time (ms)

- [ ] **Automatic report:**
  - Generate PDF/HTML with charts and metrics
  - Comparison with normative data (if available)
  - Athlete history

### 3.4 Data Export

- [ ] CSV with raw data (timestamp, force_N)
- [ ] JSON with calculated metrics
- [ ] Pyomeca/c3d-compatible format (optional)

---

## Phase 4: Validation (Weeks 5–8)

### 4.1 Technical Validation

- [ ] Verify linearity with known weights (0–100 kg in 10 kg increments)
- [ ] Verify temporal drift (measure 10 continuous minutes with fixed weight)
- [ ] Verify actual sampling rate (count samples in a time window)
- [ ] Verify noise (standard deviation at rest)
- [ ] Hysteresis test (loading/unloading)

### 4.2 Scientific Validation (paper)

- [ ] Protocol: N ≥ 20 participants
- [ ] Compare with commercial platform (Kistler, AMTI, or similar available)
- [ ] Tests: CMJ, SJ, DJ on both platforms (randomized order)
- [ ] Analysis: ICC, Bland-Altman, CV%, SEM
- [ ] Target: ICC ≥ 0.95, CV% < 5%

---

## Phase 5: Dual Force Plate (Future)

- [ ] Cut 50×60 cm plate in half → 2 plates of 50×30 cm (similar dimension to VALD FDLite: 48.5×30 cm)
- [ ] Add +4 F shear beam load cells 500 kg
- [ ] Expand reading: use all 8 ADS1256 channels (4+4) or add a second ADS1256
- [ ] Adapt firmware for 2 independent platforms (left force + right force)
- [ ] Implement bilateral asymmetry metrics in software

## Phase 6: Product (Future)

- [ ] Custom PCB design (replace breadboard)
- [ ] 3D-printed or injection-molded enclosure
- [ ] Mobile app (Flutter/React Native)
- [ ] Reproduction documentation (open-source hardware)
- [ ] Nova O2 website page

---

## Architecture Decisions

### Why ESP32-S3 and not Teensy 4.1?

| Criterion | ESP32-S3 | Teensy 4.1 |
|-----------|----------|------------|
| Cost | R$ 30–50 | R$ 150–200 |
| Integrated WiFi/BLE | ✅ | ❌ (requires extra module) |
| SPI performance | Sufficient for 1000 Hz | Better (600 MHz) |
| Arduino ecosystem | ✅ | ✅ |
| Availability in Brazil | Easy (AliExpress) | Difficult |

For a single platform at 1000 Hz, the ESP32-S3 is more than sufficient.

### Why F shear beam cells and not S-type?

| Criterion | F shear beam (with foot bolt) | S-type |
|-----------|-------------------------------|--------|
| Assembly | Simple — foot on floor, plate on top | Requires 2 plates (top + bottom) |
| Total weight | ~7 kg (1 plate 50×60) | ~13 kg (2 plates) |
| Cost | Lower (~R$ 120–200 less) | Higher (second plate + spacers + feet) |
| Commercial use | Standard in platform scales | Common in tension/compression systems |
| Precision | Equivalent for uniaxial application | Equivalent |
| Extra requirement | Rigid, flat floor | None (bottom plate levels itself) |

The F shear beam cell with foot bolt is the industry standard for platform scales. It simplifies assembly, reduces cost and weight, and is proven in millions of commercial devices. The only drawback is dependence on an adequate floor, easily addressed.

### Why ADS1256 and not HX711?

- HX711: 80 Hz maximum — **insufficient** for jump analysis
- ADS1256: up to 30,000 Hz, 24-bit — standard in research force plates

### Load cell configuration

**Option A — Single bridge (4 in parallel):**
- Simpler, 1 ADC channel
- Gives only total vertical force
- Sufficient for MVP

**Option B — 4 independent channels:**
- Each cell on a separate ADS1256 channel
- Allows COP (Center of Pressure) calculation via moments
- More complex, but more information
- **Recommended** — the ADS1256 has 8 channels; using 4 adds no cost

**Decision: Option B** — read 4 independent channels (250 Hz each in multiplexed mode, or 1000 Hz with appropriate configuration).

---

## Technical References

- [ADS1256 Datasheet](https://www.ti.com/lit/ds/symlink/ads1256.pdf)
- [ESP32-S3 Technical Reference](https://www.espressif.com/sites/default/files/documentation/esp32-s3_technical_reference_manual_en.pdf)
- [can-can-group/forceplate-hardware-code](https://github.com/can-can-group/forceplate-hardware-code)
- [force-plate-jump-analyses (Python)](https://github.com/stevenhirsch/force-plate-jump-analyses)
