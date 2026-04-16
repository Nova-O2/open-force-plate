# Technical Component Specifications — Force Plate MVP

Consolidated reference sheet for all project components. Original manufacturer specs (preserve for calibration, validation, and methods paper).

**Purchase log:** see [COMPONENTS_SELECTED.md](./COMPONENTS_SELECTED.md)
**Assembly and integration:** see [DEVELOPMENT_PLAN.md](./DEVELOPMENT_PLAN.md)
**Structural analysis:** see [STRUCTURAL_ANALYSIS.md](./STRUCTURAL_ANALYSIS.md)

---

## 1. Electronics

### 1.1 Load Cells — Decent DYX-301 500 kg (×4)

**Type:** F shear beam with foot bolt. Material: alloy steel.
**Capacity:** 500 kg per cell → 2,000 kg (19,620 N) total with 4 units.

#### Metrological specs

| Parameter | Value |
|-----------|-------|
| Output sensitivity | 2.0 ± 0.05 mV/V |
| Zero point output | ±1 % F.S. |
| Non-linearity | 0.03 % F.S. |
| Hysteresis | 0.03 % F.S. |
| Repeatability | 0.03 % F.S. |
| Creep (30 min) | 0.03 % F.S. |
| Temperature sensitivity drift | 0.03 % F.S. / 10°C |
| Zero temperature drift | 0.05 % F.S. / 10°C |
| Response frequency | 1 kHz |

#### Electrical specs

| Parameter | Value |
|-----------|-------|
| Impedance | 350 Ω |
| Insulation resistance | ≥ 5000 MΩ @ 100V DC |
| Working power | DC 5–15 V |
| Cable | Ø5 mm × 3 m shielded (4 wires: E+, E−, S+, S−) |

#### Mechanical/environmental specs

| Parameter | Value |
|-----------|-------|
| Material | Alloy steel |
| Operating temperature | −20 to 80 °C |
| Safety overload | 150% R.C. (750 kg = 7,355 N) |
| Extreme overload | 200% R.C. (1,000 kg = 9,807 N) |

#### Dimensions (manufacturer drawing)

| Dim | Value | Description |
|:---:|:-----:|-------------|
| A | 30 mm | Total length |
| B | 15 mm | Cable exit |
| C | 25 mm | Distance between mounting holes |
| D | 76 mm | Total body |
| E | 30 mm | Width |
| W | 32 mm | Base width |
| H | 32 mm | Height |
| M | M12 × 1.75 | Foot bolt thread |
| 2-Ø | Ø13 mm | Cell hole diameter |
| I | 56 mm | Base length (bearing surface) |

**Assessment:** Professional-grade specs. Non-linearity/hysteresis of 0.03% exceed the requirement (<0.05%). Impedance of 350 Ω is a perfect match for the ADS1256. Sensitivity tolerance (±0.05 mV/V) is tighter than the standard (±0.1).

---

### 1.2 ADC — ADS1256 24-bit Module (×2: 1 active + 1 backup/dual)

**Integrated chips:**
- ADC: **ADS1256IDB** (Texas Instruments) — ultra-low noise, high precision
- Voltage reference: **ADR03** 2.5V (Analog Devices) — precision reference

| Parameter | Value |
|-----------|-------|
| Resolution | 24 bits |
| Data output rate | up to 30 ksps |
| Non-linearity | ±0.0010 % |
| Input modes | 8 single-ended or 4 differential |
| Analog input range | up to 3 V |
| Communication | SPI |
| Operating voltage | 5 V |
| PGA | 1, 2, 4, 8, 16, 32, 64 |

#### Planned configuration

- Mode: 4 differential channels (1 per load cell)
- Effective rate: 1000 Hz per channel (4 ksps multiplexed, within the 30 ksps limit)
- PGA: 64 (range ±78 mV, ideal for the ~10 mV cell signal)

**Assessment:** Module with ADR03 reference is a differentiator — precision reference reduces noise compared to generic modules. Non-linearity of ±0.0010% is 30× better than the cells (0.03%), so the ADC will never be the precision bottleneck.

---

### 1.3 Microcontroller — ESP32-S3-DevKitC-1 N16R8 (×2: 1 active + 1 backup)

| Parameter | Value |
|-----------|-------|
| Processor | Dual-core Xtensa LX7, 240 MHz (CoreMark: 1181.60 dual) |
| Flash | 16 MB |
| PSRAM | 8 MB |
| SRAM | 512 KB + 16 KB RTC |
| ROM | 384 KB |
| Bus | 128-bit data bus, SIMD support |
| WiFi | 802.11 b/g/n (2.4 GHz, up to 150 Mbps) |
| Bluetooth | BLE 5.0 + Mesh (125 Kbps, 500 Kbps, 1 Mbps, 2 Mbps) |
| USB | 1× full speed USB OTG (native USB-C) |
| GPIO | 45 |
| SPI | 4× SPI (+ Dual SPI, Quad SPI, Octal SPI, QPI, OPI) |
| I2C | 2× |
| UART | 3× |
| Internal ADC | 2× 12-bit SAR, 20 channels (not used — we have external ADS1256) |
| Internal temp sensor | 1× |
| Timers | 4× 54-bit universal + 1× 52-bit system + 3× Watchdog |
| DMA | Universal (5 RX + 5 TX channels) |
| Power supply | 5V via USB-C |

**Why N16R8:** Ample memory for 1000 Hz data buffer, complex firmware, and future expansion (OTA updates, local logging, dual plate). The N8R2 variant works but leaves no margin.

#### SPI connections (ADS1256 ↔ ESP32-S3)

| ADS1256 | ESP32 GPIO |
|---------|:----------:|
| SCLK | 18 |
| MOSI (DIN) | 23 |
| MISO (DOUT) | 19 |
| CS | 5 |
| DRDY | 4 |

**Verified via vendor spec sheet (2026-04-01):** CPU, BLE, and peripherals confirmed compatible with all project requirements.

---

### 1.4 Battery — Li-ion Pack 1S2P 3.7V 5200 mAh (×2)

**Model:** Rectangular Li-ion 1S2P pack (2× 18650 cells in parallel) with integrated BMS
**Vendor:** EPB Energia Portátil Brasil (official store — ENERGIAPORTATILBRASIL, Mercado Livre)
**Purchase:** 2026-04-04 — 2 units × R$ 26.71 = R$ 53.42
**Status:** awaiting delivery

| Parameter | Value |
|-----------|-------|
| Type | Lithium-ion (Li-ion) |
| Architecture | 1S2P (2× 18650 cells in parallel) |
| Nominal capacity | 5200 mAh |
| Capacity per cell | 2600 mAh (standard 18650) |
| Nominal voltage | 3.7 V |
| Fully charged voltage | 4.2 V |
| Cutoff voltage (BMS) | typically 2.5–3.0 V |
| Integrated BMS | Yes (overcharge/overdischarge/short-circuit protection) |
| Connector | JST-XH-2P (2.54 mm) — red=+, black=− |
| Dimensions | 36 × 19 × 65 mm (rectangular) |
| Weight | ~90 g |
| Energy | 19.24 Wh |
| **Energy density** | **432 Wh/L** ✅ realistic |
| Warranty | 3 months (vendor) |

#### Spec honesty verification

| Check | Result |
|-------|:------:|
| Density < 700 Wh/L (Li-ion theoretical limit) | ✅ 432 Wh/L |
| Geometry consistent with 2× 18650 (36×18×65 mm expected) | ✅ matches |
| Weight consistent with 2× 18650 (~90g expected) | ✅ exact match |
| Capacity/cell consistent with market (2000–3500 mAh) | ✅ 2600 mAh typical |

**Estimated runtime** (actual draw ~215 mA @ 3.7V):
- Capacity 5,200 mAh (labeled) → **~24 h**
- Pessimistic capacity 4,000 mAh → ~18.6 h
- Project target: 3–4 h → **6–8× headroom**

#### Connector adaptation

Pack ships with **JST-XH-2P (2.54 mm)**; TP4056 uses **JST-PH (2.0 mm)**. Two options:
1. Swap connector: desolder JST-XH from pack, solder JST-PH (PH 2.0mm kit already purchased on AliExpress, item #10)
2. Solder wires directly to B+/B− pads on TP4056 (more robust)

#### History

- **01/04:** purchased BGB Energy 3.7V battery labeled 3000 mAh (Karina Mayumi, ML) — identified capacity overclaim (implied density 720 Wh/L, above theoretical limit). Estimated actual capacity: 1,000–1,500 mAh.
- **04/04:** initiated BGB return + purchased 2 EPB 1S2P 5200 mAh packs with verified honest specs.

**Lesson learned:** for Li-ion/LiPo batteries, always calculate energy density before buying (capacity × voltage / volume). A pack with >400 Wh/L in LiPo pouch or >700 Wh/L in cylindrical Li-ion is very likely an overclaim.

---

### 1.5 Charger — TP4056 Type-C with protection (×5 kit)

| Parameter | Value |
|-----------|-------|
| Model | TP4056 with overdischarge/overcurrent protection |
| Input | 5V via USB Type-C |
| Cutoff voltage | 4.2V ± 1% |
| Maximum charge current | 1000 mA |
| Overdischarge protection | 2.5V |
| Overcurrent protection | 3A |
| Dimensions | 2.6 × 1.7 cm |

**Connection:** B+ and B− → LiPo battery. OUT+ and OUT− → MT3608 boost (3.7V→5V) → ESP32 + ADS1256. USB Type-C → charging.
**LED:** Red = charging. Green = complete.

---

### 1.6 Boost Converter — MT3608 Step-Up 3.7V→5V (×2)

| Parameter | Value |
|-----------|-------|
| Model | MT3608 DC-DC Step-Up |
| Input | 2–24 V DC |
| Output | 5–28 V DC (adjustable via trimpot) |
| Max current | 2 A |
| Efficiency | ~93% |
| Dimensions | ~36 × 17 × 14 mm |

**Function:** Converts 3.7V from the LiPo battery to stable 5V. Required because the ADS1256 (AVDD) needs 4.75–5.25 V and the ESP32 DevKit onboard regulator needs ~4.5V minimum input.

> **🔴 BEFORE FIRST USE**
>
> Turn the blue trimpot ~20 turns counterclockwise to start with low output voltage. Connect a multimeter to VOUT+/VOUT− pins and turn slowly clockwise until reading **5.0 V**. Only then connect to the circuit. High output can damage the ESP32 or ADS1256.

---

### 1.7 Power Button — 12 mm Metal LED (×1)

| Parameter | Value |
|-----------|-------|
| Type | Metal push button, 12 mm |
| Mode | Fixed self-locking (latching — stays on/off) |
| LED voltage | 3–9 V (compatible with circuit 3.7–5V) |
| Material | Metal |
| LED | Integrated (lights when on) |

**Function:** Main platform switch. Cuts power between MT3608 and the rest of the circuit.

---

## 2. Mechanics — Structure

### 2.1 Top plate — Aluminum 5052-F

| Parameter | Value |
|-----------|-------|
| Dimensions | 600 × 500 × 6.35 mm (1/4 in) |
| Material | Al 5052-F |
| Corners | R30 rounded |
| Holes | 8× Ø11 mm, countersunk Ø20 mm × 5.5 mm depth (90°) |
| Weight | ~5.11 kg |
| Technical drawing | `hardware/cad/fab_top_plate.pdf` |

#### Al 5052-F properties

| Property | Value |
|----------|-------|
| Elastic modulus (E) | 70,300 MPa |
| Yield strength (σ_y) | 90 MPa |
| Poisson's ratio (ν) | 0.33 |
| Density (ρ) | 2,680 kg/m³ |

---

### 2.2 Bottom plate — Aluminum 3 mm

| Parameter | Value |
|-----------|-------|
| Dimensions | 527 × 396 × 3 mm |
| Material | Al 5052-F |
| Corners | 15 × 15 mm chamfers at 45° |
| Holes | 8× Ø11 mm |
| Weight | ~1.67 kg |
| Technical drawing | `hardware/cad/fab_bottom_plate.pdf` |

---

### 2.3 Steel shims (×4)

| Parameter | Value |
|-----------|-------|
| Material | Carbon steel or stainless steel |
| Dimensions | 56 × 32 × 2 mm |
| Holes | 2× Ø11 mm, 25 mm center-to-center |
| Function | Spacer between cell and top plate (distributes load, prevents aluminum crushing) |
| Technical drawing | `hardware/cad/fab_shim.pdf` |

**Note:** do not use rubber — it dampens the dynamic signal at 1000 Hz.

---

### 2.4 Turned foot bolts with collar (×4) — single machined part

| Part | Dimension |
|------|:---------:|
| Thread | M12 × 1.75, Ø12 mm, 32 mm length (= cell height) |
| Collar | Ø20 mm, 5 mm height (stop — rests against cell) |
| Chamfer | Ø20 → Ø60 mm, 6 mm height (~17°) |
| Base | Ø60 mm, 8 mm thickness |
| Rubber pad | Ø60 mm × 1 mm neoprene (glued after machining) |
| Total height | 52 mm |
| Material | Carbon steel or stainless steel (Ø60 mm bar stock) |
| Technical drawing | `hardware/cad/fab_foot_piece.pdf` |

**Function:** Support/leveling. No lock nut — collar acts as mechanical stop; platform weight locks position.

---

### 2.5 Structural reinforcement — Square tubes (×2)

| Parameter | Value |
|-----------|-------|
| Material | Extruded aluminum |
| Section | 30×30×2 mm or 35×35×2 mm (subject to availability) |
| Length | ~527 mm each |
| Quantity | 2 tubes |
| Position | Longitudinal (X-axis), at Y=194 mm and Y=306 mm from top plate |
| Bonding | Structural epoxy |

**Function:** Creates box section with both plates (flanges). I_total = 1,062,162 mm⁴ (118× the rigidity of the plate alone).

---

### 2.6 Bolts — M10 × 50 DIN 7991 (×8)

| Parameter | Value |
|-----------|-------|
| Standard | DIN 7991 (flat countersunk Allen head) |
| Dimension | M10 × 50 mm |
| Class | 8.8 (minimum) |
| Head | Ø20 mm (matches top plate countersink) |
| Includes | M10 nut + washer (×8 each) |

---

### 2.7 Structural epoxy

| Parameter | Value |
|-----------|-------|
| Type | Two-part structural epoxy |
| Compatible brands | Araldite Professional, Loctite EA 9461, or equivalent |
| Shear strength | ≥ 20 MPa (typically 20–30 MPa) |
| Cure | 24 h under pressure (clamps) |
| Preparation | Sand surfaces (80-grit), degrease (isopropyl alcohol) |

---

## 3. Complete System — Theoretical Resolution

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
```

**VALD FDLite comparison:** ~0.15 N → **we match or exceed**.

---

## 4. Power Architecture

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

- **USB-C mode (primary):** 5V direct from USB powers everything. MT3608 inactive.
- **Battery mode (BLE):** MT3608 converts 3.7V→5V. Everything works without a cable.

---

## 5. Prototyping Tools and Accessories

### Soldering and measurement

| Item | Spec |
|------|------|
| Soldering iron | Exbom 60W, adjustable, 5 tips, with stand |
| Solder | 60/40 (Sn/Pb) with flux core, 0.8 mm, 80 g |
| Multimeter | Multimeter kit + voltage pen + clamp ammeter |
| Soldering temperature | 300–350 °C for electronic components |

### Prototyping

| Item | Spec |
|------|------|
| Breadboard | 830 tie points |
| Jumper wires | Dupont 20 cm, flexible, 24 AWG copper, M-M/M-F/F-F |
| Connectors | XH 2.54 mm, 4-pin, 20 cm, F5 + M5 |
| Resistor kit | 1/4 W 1%, assorted values (300 pcs) |

---

## 6. Revision History

| Rev. | Date | Description |
|:----:|:----:|-------------|
| 1.0 | 2026-04-04 | Initial consolidation of all specs — recovered from git (commit 3f66aa7^) + integration of mechanical dimensions from DEVELOPMENT_PLAN and structural properties from STRUCTURAL_ANALYSIS |
