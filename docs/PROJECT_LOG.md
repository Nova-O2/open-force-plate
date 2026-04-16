# Project Log — Nova O2 Force Platform

Chronological project record. Most recent entry at the top.

For technical specs: [COMPONENT_SPECS.md](./COMPONENT_SPECS.md) | For costs: [COMPONENTS_SELECTED.md](./COMPONENTS_SELECTED.md) | For roadmap: [DEVELOPMENT_PLAN.md](./DEVELOPMENT_PLAN.md)

---

## 2026-04-16 — Components in hand, mechanical assembly begins

- 5052-F aluminum plates picked up at Casa dos Metais (R$550 — 6.35mm top + 3mm bottom)
- All AliExpress + Mercado Livre components in hand, except DYX-301 load cells
- Load cells already in Brazil — expected to arrive this week
- Turned feet on hold until load cells arrive to confirm measurements before ordering from machinist

## 2026-04-14 — AliExpress delivery

- 11 of 12 AliExpress items received in a single batch: ADS1256, ESP32-S3, TP4056, MT3608, button, breadboards, jumpers, XH/PH connectors, resistors, LEDs
- DYX-301 load cells not included in this batch (separate seller/shipment)

## 2026-04-11 — Replacement batteries received

- Received 2× Li-ion 1S2P 5200mAh batteries with BMS (replacement for the returned BGB battery, which was identified as a capacity overclaim)

## 2026-04-04 — Mechanical design Rev. 2.0

Complete overhaul of mechanical design with structural analysis:

- Material change: 6061-T6 aluminum → 5052-F (local availability), Al tubes → 1020 steel (off-the-shelf)
- Top plate thickness: 6mm → 6.35mm (1/4" — available standard)
- Box section (2× 35×35mm steel tubes) reduces deflection from 21mm to <0.2mm
- Correction: M10×45 screws → M10×50, 30mm chamfer → 15mm
- Structural analysis recalculated with transformed section (n = 2.845) — FS >4 in all scenarios
- Local components shopping list created (~R$500)
- BGB Energy 3000mAh battery identified as overclaim (720 Wh/L, above theoretical Li-ion limit) — returned
- Privacy cleanup: supplier data moved to gitignored file

## 2026-04-01/02 — Mechanical design Rev. 1.0 + purchases

**Component selection and purchases (01/04):**
- Components selected: DYX-301 500kg (shear beam), ADS1256 24-bit ADC, ESP32-S3 N16R8
- Architecture decision: AMS1117 LDO replaced by MT3608 boost converter (stable 5V from LiPo 3.3–4.2V)
- AliExpress order placed: 12 items, R$2,009
- Mercado Livre order placed: 7 items (tools + battery), R$369
- Docs reorganized: specs separated from purchases, clear responsibilities between files

**Mechanical design (01–02/04):**
- Design finalized: 62° angle (half-plate diagonal), single bottom plate, 56×32mm shims
- Fabrication drawings generated (3 PDFs with Nova O2 branding): top plate, bottom plate, turned foot
- Turned foot specs: M12×1.75 shaft, ~17° chamfer, Ø60×8mm base, Ø20×5mm collar, 1mm rubber pad

## 2026-03-28 — Project start

- Project created: open-source force platform for sports science
- Initial specs defined: uniaxial (Fz), 1000 Hz, 24-bit, 2000 kg, USB-C + BLE
- Positioning: comparable to VALD FDLite (~R$60,000) at a fraction of the cost (~R$2,500)
- 6-phase development plan: hardware → firmware → software → validation → dual plate → product
