# Shopping List — Mechanical Assembly

**Date:** 2026-04-06 (last updated 2026-06-10 — cascade pós-montagem mecânica)
**Status:** ✅ **MECHANICAL PROCUREMENT COMPLETE.** All mechanical components purchased and assembled (full assembly 2026-06-08). Final purchases: 2nd Araldite lot (R$ 62 — 2026-05-20), foot zincagem (R$ 105 — TL Tratamento Superficial, 2026-05-25), 304 shim sheet self-sourced (R$ 79,90 — MALUCOMERCIAL/ML, received 2026-05-29), shim cut+drill (R$ 180 — AL Usinagem, delivered 2026-06-03). ML hardware delivered 2026-05-12/13. Consumables resolved from household stock (P24 sandpaper, acetone, Tekbond 793) — not itemized.
**Total spent:** R$ 2.758,76 (R$ 550 plates + R$ 1.480 AL Usinagem + R$ 136,19 ML hardware + R$ 103,67 tube + R$ 124 epoxy 4× 23 g + R$ 105 zincagem + R$ 79,90 shim sheet + R$ 180 shim cut+drill)

> **Rev 3.0 changes (2026-05-08):**
> - Fastening: M10×50 class 8.8 → **M10×60 inox 304** + Parlock + arruela 304 (galvanic compatibility + cyclic durability)
> - Shims: 4 → **8 units** (mirror top + bottom, bearing distribution on both Al 5052-F faces)
> - Material: shims now mandatory **inox 304** (was "carbon or stainless")
> - Foot piece: bar Ø60 → Ø55 + base vertical wall knurled (AL Usinagem fab choices)
> - Plate chamfer: perimeter chamfer added (top 2.12 mm both faces, bottom 1.5 mm bottom face only)

> **Rev 3.1 changes (2026-05-18):**
> - Structural tube: 1020 carbon steel 35×35×2 mm → **stainless steel 304 35×35×1.5 mm**, 500 mm length (off-the-shelf at Real Fortaleza Hidráulica, Jacareí). Completes "inox 304 throughout" — the tube was the last carbon-steel exception.
> - Epoxy: specified **Araldite Professional 90 min, 2× 23 g** (Tekbond BRAP000)
> - Surface prep: sandpaper P80 → **P40–P60** (coarse abrasion for stainless passive layer)

---

## Metal Supplier / Plate Cutting (~R$ 230)

| # | Item | Specification | Qty | Budget (R$) |
|---|------|--------------|:---:|----------:|
| 1 | Top plate | Al 5052-F, 603×503 mm, 6.35 mm (1/4"), rounded corners R30 | 1 | **410.00** |
| 2 | Bottom plate | Al 5052-F, 530×399 mm, 3 mm, chamfered corners 15×15 at 45° | 1 | **140.00** |
| 3 | Square tube ✅ | **Stainless steel 304, 35×35×1.5 mm**, 2 pieces of 500 mm (from 1 m bar) — Rev 3.1, Real Fortaleza Hidráulica 2026-05-18 | 2 | 103,67 |

> **💡 Quote received (2026-04-06)**
>
> **Supplier:** Casa dos Metais Ltda
> Items 1 and 2 quoted with commercial dimensions (+3 mm allowance). Total plates: **R$ 550.00**.
> Corner cutting (R30 and 45° chamfer) and steel tubes still to be quoted — possibly a different supplier.

> **ℹ️ Material changes (2026-04-06)**
>
> **Aluminum alloy:** 6061-T6 not available locally → 5052-F. Identical stiffness (E ~70 GPa), lower yield strength (90 vs 276 MPa) but FS > 4 with the box section.
> **Tubes:** Square aluminum tubes hard to source → standard carbon steel. Stiffer (+23%), cheaper, off-the-shelf product. Adds +1.4 kg to total weight.

**Bring PDFs:** `hardware/cad/fab_top_plate.pdf`, `hardware/cad/fab_bottom_plate.pdf`

> **📝 Note**
>
> Request cutting and rounding/chamfering at the metal supplier. Drilling and countersinking to be done at home with a jig for higher precision.

---

## Machine Shop / Turner — AL Usinagem (R$ 1,480 — RECEIVED 2026-05-08)

| # | Item | Specification | Qty | Cost (R$) |
|---|------|--------------|:---:|----------:|
| 4 | Turned foot piece with collar | Bar stock **Ø55 mm** (Rev 3.0 — was Ø60), base vertical wall **knurled** | 4 | **1,120** (R$ 280 each) |
| 4b | Plate finishing service | Drilling 8× Ø11mm + countersinking 8× Ø20×5.5mm + corner R30/chamfer + perimeter chamfer | 1 lot | **360** |

**Part dimensions (bottom to top) — Rev 3.0:**

| Section | Dimension |
|---------|-----------|
| Rubber | **Ø55 mm** × 1 mm neoprene (glued after machining) — Rev 3.0 |
| Base | **Ø55 mm** × 8 mm — vertical wall knurled (Rev 3.0) |
| Chamfer | **Ø55→Ø20**, 6 mm height (~16°) — Rev 3.0 |
| Collar | Ø20 mm × 5 mm (mechanical stop) |
| Thread | M12×1.75, Ø12 mm, 32 mm length |
| **Total height** | **52 mm** |

**Bring PDF:** `hardware/cad/fab_foot_piece.pdf`

---

## Stainless Steel Shims — self-sourced sheet + AL Usinagem cut/drill (✅ RECEIVED 2026-06-03)

| # | Item | Specification | Qty | Cost (R$) |
|---|------|--------------|:---:|----------:|
| 5a | 304 sheet stock ✅ | Inox 304, 300×100×**2 mm** (final empirical thickness — see [`COMPONENT_SPECS.md`](./COMPONENT_SPECS.md) §2.3.1) — MALUCOMERCIAL/MercadoLivre, received 2026-05-29 | 1 | **79,90** |
| 5b | Cut + drill service ✅ | 8 shims 56×32×2 mm, 2 through holes Ø11 mm each, 25 mm center-to-center — AL Usinagem, sheet delivered 2026-05-29, parts received 2026-06-03 | 8 | **180,00** |

> **✅ Process gate (Rev 3.0) honored:** shims fabricated only after empirical box section measurement (2026-05-26: ~36 mm − cell 32 mm → 2+2 mm mirror). Sourcing pivoted on 2026-05-26 from "AL Usinagem quotes everything" to self-sourced sheet + AL machining only. Drawing re-render (`fab_shim.pdf` at 2 mm) still pending — documentation debt, parts already made to correct spec.

---

## Fasteners / Hardware — MercadoLivre (R$ 136,19 — ✅ DELIVERED 2026-05-12/13)

| # | Item | Specification | Qty (kit) | Cost (R$) | Loja |
|---|------|--------------|:---:|----------:|------|
| 6 | Flat-head Allen bolt | **M10×60** DIN 7991 **inox 304 A2** passivated (Rev 3.0 — was M10×50 cl 8.8), full thread, chave Allen 6 mm | 1 kit (10 un) | **76,05** | MIXPARAFUSOS |
| 7 | Locknut M10 Parlock | **All-metal locknut** (Rev 3.0 — was hex nut DIN 934), inox 304, chave 17 mm | 2 kits (20 un) | **37,14** (16% off) | EMAIFIX |
| 8 | M10 plain washer | **Inox 304** (Rev 3.0 — was unspec), polido | 2 kits (20 un) | **23,00** | USINIK (loja oficial) |
| 9 | HSS metal drill bit Ø11 mm | (already in toolkit, not re-ordered) | — | — | — |
| 10 | 90° conical countersink Ø20 | (drilling done by AL Usinagem, not needed local) | — | — | — |

> **All 3 ML purchases:** frete grátis. Subtotal R$ 136,19. Spare quantities (2 bolts + 12 nuts + 12 washers) for maintenance over device lifetime.

---

## Materials and Consumables (~R$ 110)

| # | Item | Specification | Qty | Cost (R$) |
|---|------|--------------|:---:|----------:|
| 11 | Structural epoxy adhesive ✅ | **Araldite Profissional 90 min, 23 g bisnaga** (Tekbond BRAP000) — 2× 2026-05-19 (session 1) + 2× 2026-05-20 (session 2), Real Fortaleza Hidráulica | 4 | **124,00** (R$ 31 cada) |
| 12 | Rubber for feet ✅ | Resolved with household scrap + **Tekbond 793 cianoacrilato** (contact neoprene adhesive failed first — see LOG 2026-05-26) | 4 | 0 (household stock) |
| 13–15 | Consumables ✅ | Resolved from household stock during bonding sessions (P24 sandpaper, acetone degrease, clamping load) — not itemized | — | 0 |
| 16 | Foot zincagem service ✅ | Anti-corrosion zinc plating (meio banho), 4 feet — TL Tratamento Superficial, delivered 2026-05-25 | 1 lot | **105,00** |

---

## Summary by Supplier

| Supplier | Items | Subtotal | Status |
|----------|:-----:|----------:|--------|
| Casa dos Metais (Al plates) | 1–2 | **R$ 550** | ✅ Purchased 2026-04-16 |
| AL Usinagem (plate finishing + turned feet) | 1–2 finishing + 4 | **R$ 1.480** | ✅ Received 2026-05-08 |
| MALUCOMERCIAL/ML (304 shim sheet 300×100×2 mm) | 5a | **R$ 79,90** | ✅ Received 2026-05-29 |
| AL Usinagem (cut + drill 8 shims) | 5b | **R$ 180** | ✅ Received 2026-06-03 |
| Real Fortaleza Hidráulica (stainless 304 tube, Rev 3.1) | 3 | **R$ 103,67** | ✅ Purchased 2026-05-18 |
| Real Fortaleza Hidráulica (Araldite Profissional 4× 23 g) | 11 | **R$ 124,00** | ✅ Purchased 2026-05-19 + 2026-05-20 |
| MercadoLivre (fasteners inox 304, Rev 3.0) | 6–8 | **R$ 136,19** | ✅ Delivered 2026-05-12/13 |
| TL Tratamento Superficial (foot zincagem) | 16 | **R$ 105** | ✅ Delivered 2026-05-25 |
| Materials (consumables) | 12–15 | R$ 0 | ✅ Household stock |
| **Total spent (mechanical complete)** | | **R$ 2.758,76** | ✅ Assembly done 2026-06-08 |

---

## Purchase Checklist

- [x] Casa dos Metais — close purchase of 2 Al plates (R$ 550) — picked up 2026-04-16
- [x] AL Usinagem — measurement check + plates finishing (R30/chamfer + drilling + countersinking + perimeter chamfer Rev 3.0) + 4 foot pieces (Ø55 + base wall knurled) — received 2026-05-08, R$ 1,480
- [x] MercadoLivre fastening (Rev 3.0) — M10×60 inox 304 + Parlock + arruela 304 — ordered 2026-05-08, R$ 136,19, delivered 2026-05-12/13
- [x] Real Fortaleza Hidráulica — stainless 304 tube 35×35×1.5 mm (1 m bar) — purchased 2026-05-18, R$ 103,67
- [x] Real Fortaleza Hidráulica — Araldite Profissional 90 min, 4× 23 g total — purchased 2026-05-19 + 2026-05-20, R$ 124,00
- [x] TL Tratamento Superficial — foot zincagem (meio banho) — delivered 2026-05-25, R$ 105
- [x] MALUCOMERCIAL/ML — 304 sheet 300×100×2 mm (shim stock) — received 2026-05-29, R$ 79,90
- [x] AL Usinagem — cut + drill 8 shims 56×32×2 mm — delivered 2026-06-03, R$ 180
- [x] Materials — consumables resolved from household stock (P24, acetone, Tekbond 793)

> **✅ Process gate honored (closed 2026-06-08):**
>
> 1. ~~Wait for load cells to arrive (AliExpress)~~ ✅ Received 2026-04-23 (4 units, no damage)
> 2. ✅ Stainless 304 tube received (2026-05-18) — cut into 2× 500 mm
> 3. ✅ Bonding sessions 1+2 (2026-05-19 + 2026-05-20), cure inspected OK 2026-05-25
> 4. ✅ Box section measured post-cure 2026-05-26: ~36 mm internal
> 5. ✅ Final shim thickness: (36 − 32) / 2 = **2 mm**
> 6. ✅ `COMPONENT_SPECS.md` §2.3 updated to 2 mm (⏳ `fabrication_drawings.py` + `fab_shim.pdf` re-render still pending — debt)
> 7. ✅ 8 shims fabricated at 2 mm (AL Usinagem, delivered 2026-06-03)
> 8. ⚠️ Full assembly done 2026-06-08 **without torque wrench** — 20–25 N·m spec not instrumentally verified (accepted for MVP)
