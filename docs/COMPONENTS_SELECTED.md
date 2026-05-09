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

## AL Usinagem (Jacareí) — Received 2026-05-08

| # | Item | Qty | Cost (R$) |
|---|------|:---:|----------:|
| 1 | Turned foot piece with collar — bar Ø55 mm, base vertical wall knurled (Rev 3.0) | 4 | **1,120** (R$ 280 each) |
| 2 | Plate finishing service — 8× Ø11 mm drilling + 8× Ø20×5.5 mm countersinking + corner R30/15×15 chamfer + perimeter chamfer (top 2.12 mm both faces, bottom 1.5 mm bottom face only) | 1 lot | **360** |
| | | **Subtotal** | **1,480** |

**Discrepancies from Rev 2.0 spec (accepted as Rev 3.0):**
- Foot piece bar Ø60 → Ø55 (machine shop preference for available stock)
- Foot piece: base vertical wall knurled (added by machine shop, accepted as improvement for grip during sensor threading)
- Plates: perimeter chamfer added (acabamento for safe handling — sketch by AL Usinagem in spec anexo)

---

## Mercado Livre — Purchased 2026-05-08 (Rev 3.0 fastening)

| # | Item | Vendor (loja ML) | Qty (kit) | Cost (R$) |
|---|------|------|:---:|----------:|
| 1 | M10×60 DIN 7991 inox 304 A2 (Allen cabeça chata, passivado) | MIXPARAFUSOS | 1 (10 un) | **76,05** |
| 2 | M10 Parlock all-metal locknut inox 304 (chave 17 mm) | EMAIFIX | 2 (20 un) | **37,14** (16% off) |
| 3 | M10 plain washer inox A2/304 polido | USINIK (loja oficial) | 2 (20 un) | **23,00** |
| | **Frete** | (todos os 3 vendedores) | | grátis |
| | | **Subtotal** | | **136,19** |

**Rev 3.0 design rationale:**
- Stainless 304 throughout (parafuso + porca + arruela): galvanic compatibility with Al 5052-F plates (vs Rev 2.0 cl 8.8 carbon steel which corrodes in contact with aluminum)
- Parlock all-metal locknut: anti-vibration without nylon degradation, reusable >50 cycles, suitable for cyclic athlete impact loading
- M10×60 (vs Rev 2.0 M10×50): +10 mm to accommodate added bottom shim in stack (44.35 mm Rev 3.0 vs 43.35 mm Rev 2.0)

**Discarded purchase (same session):** M10×40 DIN 7991 inox 304 (Belenus, LUTEC) — incorrect length, would not reach nut after stack. Switched to M10×60.

---

## Mechanical Components (Rev 3.0 baseline)

| # | Item | Qty | Status | Cost (R$) |
|---|------|:---:|--------|----------:|
| 1 | 5052-F aluminum top plate, 600×500mm, 6.35mm (1/4") | 1 | ✅ Casa dos Metais 2026-04-16 | 410 |
| 2 | 5052-F aluminum bottom plate, 527×396mm, 3mm | 1 | ✅ Casa dos Metais 2026-04-16 | 140 |
| 3 | Plate finishing service (drilling + countersinking + corner cut + perimeter chamfer Rev 3.0) | 1 lot | ✅ AL Usinagem 2026-05-08 | 360 |
| 4 | Turned feet with collar (Rev 3.0: bar Ø55 + base wall knurled) | 4 | ✅ AL Usinagem 2026-05-08 | 1,120 |
| 5 | **Stainless 304 shims** 56×32 mm × **1.5 mm nominal** (Rev 3.0 — empirical, see COMPONENT_SPECS §2.3.1), 8 units (4 top + 4 bottom mirror) | 8 | ⏳ AL Usinagem quote (Rev 3.0) | TBD (~150–200) |
| 6 | **M10×60 DIN 7991 inox 304** + Parlock 304 + arruela 304 (Rev 3.0) | 8+8+8 | 🚚 ML 2026-05-08 awaiting | 136 |
| 7 | Neoprene rubber discs Ø55 mm × 1 mm (Rev 3.0 — was Ø60) | 4 | ⏳ TBD | ~10 |
| 8 | 1020 carbon steel square tube, 35×35×2mm, ~527mm | 2 | ⏳ Pending | ~25 |
| 9 | Structural epoxy adhesive (Araldite Professional 24ml or equiv.) | 1 | ⏳ Pending | ~25 |
| | | **Spent + committed** | | **R$ 2,166** |
| | | **+ Pending estimate** | | ~R$ 60 + AL shims (~150–200) |
| | | **Mechanical total Rev 3.0** | | **~R$ 2,376–2,426** |

> **Cost increase vs Rev 2.0 estimate (was ~R$ 500 mechanical):** ~+R$ 1,876. Drivers: (a) AL Usinagem services R$ 1,480 — first contracted machining, replaces self-fab estimate of ~R$ 180 (feet + shims); (b) inox 304 hardware R$ 136 (vs ~R$ 30 cl 8.8 estimate); (c) shim quantity 4 → 8 (mirror config) + material upgrade to inox 304. Trade-off accepted: precision/durability/galvanic compatibility from professional machining + corrosion-resistant fastening justify the cost vs hand-fab + carbon steel.

---

## Unit Cost — 1 Platform Rev 3.0

| Category | Cost (R$) |
|----------|----------:|
| Electronics (AliExpress 2026-04-01: cells + ADS1256 + ESP32 + power) | ~1,300 |
| Battery replacement (ML 2026-04-04: 1S2P 5200 mAh × 2) | ~55 |
| Mechanical (Rev 3.0 — see breakdown above) | ~2,376–2,426 |
| **Total Rev 3.0 unit cost** | **~R$ 3,731–3,781** |

> **Vs Rev 2.0 estimate (R$ 1,858):** +R$ 1,873–1,923 (≈ +100%). The increase reflects the shift from "self-fab everything" (Rev 2.0 estimate assumed home drilling/countersinking + carbon steel hardware + machinist quote ~R$ 160) to "outsource precision work + use corrosion-resistant materials" (Rev 3.0 actual: AL Usinagem R$ 1,480 + inox 304 R$ 136). Decision rationale documented in `PROJECT_LOG.md` 2026-05-08 entry.

> **Comparison with commercial:**

| | Nova O2 | VALD FDMini | VALD FDLite |
|---|------:|----------:|----------:|
| Cost | ~R$ 3,750 (Rev 3.0) | ~R$ 30,000 | ~R$ 60,000 |
| Capacity | 2000 kg | 1000 kg | 2000 kg |
| Resolution | ~0.075–0.15 N | ~0.15 N | ~0.15 N |
| Connectivity | USB-C + BLE | USB | USB |

For dual plate (Phase 5): +4 cells + 1 ADS1256 ≈ +R$ 900.
