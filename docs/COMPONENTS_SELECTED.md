# Selected Components — Force Plate MVP

Purchase dates: 2026-04-01 (main order), 2026-04-04 (battery replacement)

**Full technical specs for each component:** see [COMPONENT_SPECS.md](./COMPONENT_SPECS.md).
**Power architecture and mounting dimensions:** see [DEVELOPMENT_PLAN.md](./DEVELOPMENT_PLAN.md).
**Suppliers and prices:** `suppliers_private.md` (gitignored, not versioned).

---

## AliExpress — Purchased 2026-04-01

| # | Item | Qty |
|---|------|:---:|
| 1 | Decent DYX-301 500kg load cells | 4 |
| 2 | ADS1256 24-bit module (ADS1256IDB + ADR03) | 2 |
| 3 | ESP32-S3-DevKitC-1 N16R8 (with pin headers) | 2 |
| 4 | TP4056 Type-C with protection (kit of 5) | 1 |
| 5 | MT3608 boost converter (standard) | 2 |
| 6 | 12mm metal self-locking LED button 3-9V | 1 |
| 7 | 830-point breadboard (kit of 3) | 1 |
| 8 | Dupont jumper wires 20cm flexible 24AWG | 1 |
| 9 | XH 2.54mm 4-pin connectors 20cm (F5+M5) | 1 |
| 10 | PH 2.0mm connectors (battery→TP4056) | 1 |
| 11 | 300-piece resistor kit 1/4W 1% metal film | 1 |
| 12 | Pre-wired 5mm LED kit 12V (30pcs, 6 colors) | 1 |

---

## Mercado Livre — Purchased 2026-04-01

| # | Item | Qty |
|---|------|:---:|
| 1 | ~~BGB Energy LiPo 3.7V battery (labeled 3000mAh)~~ — **RETURNED** (overclaim, replaced) | 1 |
| 2 | Exbom 60W adjustable soldering iron + 5 tips + stand 127V | 1 |
| 3 | 60/40 solder with flux 0.8mm 80g | 1 |
| 4 | Crimping pliers kit + wire stripper + 1200 ferrule terminals | 1 |
| 5 | Straight round-nose pliers 6.1/2" Gedore Red | 1 |
| 6 | Digital multimeter kit + voltage pen + clamp ammeter | 1 |

---

## Mercado Livre — Purchased 2026-04-04 (battery replacement)

| # | Item | Qty |
|---|------|:---:|
| 1 | Li-ion 1S2P 3.7V 5200mAh pack with BMS + JST-XH-2P (36×19×65mm) | 2 |

**Reason:** replacement for the BGB Energy 3000mAh battery (01/04), identified as a capacity overclaim (claimed energy density of 720 Wh/L, above the theoretical Li-ion limit). The 1S2P replacement packs have a realistic energy density (432 Wh/L), 2× 18650 cells of 2,600 mAh each, integrated BMS, and geometry and weight consistent with specs.

---

## Buy Locally (when AliExpress order arrives)

| # | Item | Qty | Est. (R$) |
|---|------|:---:|----------:|
| 1 | 5052-F aluminum top plate, 600×500mm, 6.35mm (1/4"), R30 corners | 1 | ~150 |
| 2 | 5052-F aluminum bottom plate, 527×396mm, 3mm, 15×15 chamfered corners | 1 | ~60 |
| 3 | 2mm steel shims (56×32mm, 2× Ø11mm holes, 25mm center-to-center) | 4 | ~20 |
| 4 | M10×50 Allen countersunk screws DIN 7991 + M10 nuts + washers (8+8+8) | 1 | ~30 |
| 5 | Ø11mm drill bit + 90° countersink M10 (Ø20) | 1 | ~20 |
| 6 | Turned feet with collar Ø20×5mm (single piece, machinist) | 4 | ~160 |
| 7 | Neoprene rubber discs Ø60mm × 1mm | 4 | ~10 |
| 8 | 1020 carbon steel square tube, 35×35×2mm, ~527mm | 2 | ~25 |
| 9 | Structural epoxy adhesive (Araldite Professional 24ml or equiv.) | 1 | ~25 |
| | | **Subtotal** | **~R$ 500** |

---

## Unit Cost — 1 Platform (without tools, without backups)

**~R$ 1,858**

| | Nova O2 | VALD FDMini | VALD FDLite |
|---|------:|----------:|----------:|
| Cost | R$ 1,858 | ~R$ 30,000 | ~R$ 60,000 |
| Capacity | 2000 kg | 1000 kg | 2000 kg |
| Resolution | ~0.075–0.15 N | ~0.15 N | ~0.15 N |
| Connectivity | USB-C + BLE | USB | USB |

For dual plate (Phase 5): +4 cells + 1 ADS1256 ≈ +R$ 900.
