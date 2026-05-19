# Shopping List — Mechanical Assembly

**Date:** 2026-04-06 (last updated 2026-05-19 — Araldite Profissional adquirido)
**Status:** Aluminum plates + 4 turned foot pieces received from AL Usinagem (R$ 1,480 — 2026-05-08). MercadoLivre hardware ordered (R$ 136,19, awaiting delivery): M10×60 inox 304 + Parlock 304 + arruela 304. Stainless 304 tube received (R$ 103,67 — Real Fortaleza Hidráulica, 2026-05-18). Structural epoxy received (R$ 62,00 — Araldite Profissional 2× 23 g, Real Fortaleza Hidráulica, 2026-05-19). Pending: 8 stainless 304 shims (1.5 mm nominal — empirical, AL Usinagem quote) + remaining consumables (sandpaper P40–P60 + isopropyl alcohol + bar clamps).
**Total spent so far:** R$ 2,332 (R$ 550 plates + R$ 1,480 AL Usinagem + R$ 136 ML hardware + R$ 104 tube + R$ 62 epoxy)

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

## Stainless Steel Shims — AL Usinagem (Rev 3.0 — quote pending)

| # | Item | Specification | Qty | Est. (R$) |
|---|------|--------------|:---:|----------:|
| 5 | Stainless 304 shim | **Inox 304** (Rev 3.0 — galvanic), 56×32 mm, **1.5 mm nominal** thickness (final empirical — see [`COMPONENT_SPECS.md`](./COMPONENT_SPECS.md) §2.3.1), 2 through holes Ø11 mm, 25 mm center-to-center | **8** (4 top + 4 bottom mirror — Rev 3.0) | TBD (AL Usinagem quote — fab after empirical box section height measurement) |

**Bring PDF:** `hardware/cad/fab_shim.pdf` (after re-render with Rev 3.0 dimensions)

> **⚠️ Process gate (Rev 3.0):** Do NOT order shims at 1.5 mm before measuring the bonded box section. Tube + epoxy + cell tolerance can shift stack ±0.5 mm. See COMPONENT_SPECS §2.3.1 for the 7-step empirical derivation procedure.

---

## Fasteners / Hardware — MercadoLivre (R$ 136,19 — ORDERED 2026-05-08, awaiting delivery)

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

| # | Item | Specification | Qty | Est. (R$) |
|---|------|--------------|:---:|----------:|
| 11 | Structural epoxy adhesive ✅ | **Araldite Profissional 90 min, 23 g bisnaga** (Tekbond BRAP000) — NOT Hobby/Massa/Fix/Transparente — Real Fortaleza Hidráulica 2026-05-19 | 2 | **62,00** (R$ 31 cada) |
| 12 | Neoprene rubber | Ø60 mm × 1 mm disc (cut from sheet if needed) | 4 | ~10 |
| 13 | Metal sandpaper | **P40–P60 grit** (coarse — stainless 304 passive layer; not P80) | 2 | ~5 |
| 14 | Isopropyl alcohol | Degrease surfaces before bonding | 1 | ~5 |
| 15 | Bar clamps (grampo sargento) | For 24 h clamping pressure during epoxy cure | 4–6 | ~40 |

---

## Summary by Supplier

| Supplier | Items | Subtotal | Status |
|----------|:-----:|----------:|--------|
| Casa dos Metais (Al plates) | 1–2 | **R$ 550** | ✅ Purchased 2026-04-16 |
| AL Usinagem (plate finishing + turned feet) | 1–2 finishing + 4 | **R$ 1,480** | ✅ Received 2026-05-08 |
| AL Usinagem (8 stainless 304 shims, Rev 3.0) | 5 | TBD | ⏳ Quote pending — fab after empirical measurement |
| Real Fortaleza Hidráulica (stainless 304 tube, Rev 3.1) | 3 | **R$ 103,67** | ✅ Purchased 2026-05-18 |
| Real Fortaleza Hidráulica (Araldite Profissional 2× 23 g) | 11 | **R$ 62,00** | ✅ Purchased 2026-05-19 |
| MercadoLivre (fasteners inox 304, Rev 3.0) | 6–8 | **R$ 136,19** | 🚚 Ordered 2026-05-08, awaiting delivery |
| Materials (remaining consumables) | 12–15 | ~R$ 60 | ⏳ To buy |
| **Total spent so far** | | **R$ 2,332** | |
| **Pending estimate** | | ~R$ 60 + AL shims | |

---

## Purchase Checklist

- [x] Casa dos Metais — close purchase of 2 Al plates (R$ 550) — picked up 2026-04-16
- [x] AL Usinagem — measurement check + plates finishing (R30/chamfer + drilling + countersinking + perimeter chamfer Rev 3.0) + 4 foot pieces (Ø55 + base wall knurled) — received 2026-05-08, R$ 1,480
- [x] MercadoLivre fastening (Rev 3.0) — M10×60 inox 304 + Parlock + arruela 304 — ordered 2026-05-08, R$ 136,19, awaiting delivery
- [x] Real Fortaleza Hidráulica — stainless 304 tube 35×35×1.5 mm (1 m bar) — purchased 2026-05-18, R$ 103,67
- [x] Real Fortaleza Hidráulica — Araldite Profissional 90 min, 2× 23 g — purchased 2026-05-19, R$ 62,00
- [ ] AL Usinagem — 8 stainless 304 shims (1.5 mm nominal — empirical, see process gate below)
- [ ] Materials — P40–P60 sandpaper + isopropyl alcohol + bar clamps

> **⚠️ Process gate before ordering shims (Rev 3.0):**
>
> 1. ~~Wait for load cells to arrive (AliExpress)~~ ✅ Received 2026-04-23 (4 units, no damage)
> 2. ✅ Stainless 304 tube received (2026-05-18) — cut into 2× 500 mm + measure dimensions with caliper
> 3. Bond plates+tubes with structural epoxy (24 h cure)
> 4. Measure bonded box section height at 4 corners + cell H actual (DYX-301)
> 5. Compute final shim thickness: `(box_height − cell_H) / 2`
> 6. If ≠ 1.5 mm: update `COMPONENT_SPECS.md` §2.3 + `fabrication_drawings.py` + re-render `fab_shim.pdf` (additional commits on Rev 3.0 branch)
> 7. **Then** order 8 inox 304 shims at measured thickness from AL Usinagem
> 8. Test-fit single corner with M10×60 + Parlock + arruela at torque 20–25 N·m before assembly of 4 cantos
