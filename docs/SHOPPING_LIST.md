# Shopping List — Mechanical Assembly

**Date:** 2026-04-06
**Status:** Aluminum plates purchased and picked up (Casa dos Metais). AliExpress received (except DYX-301 load cells). Pending: load cells + turned feet + local fasteners/materials.
**Total budget:** ~R$ 875

---

## Metal Supplier / Plate Cutting (~R$ 230)

| # | Item | Specification | Qty | Budget (R$) |
|---|------|--------------|:---:|----------:|
| 1 | Top plate | Al 5052-F, 603×503 mm, 6.35 mm (1/4"), rounded corners R30 | 1 | **410.00** |
| 2 | Bottom plate | Al 5052-F, 530×399 mm, 3 mm, chamfered corners 15×15 at 45° | 1 | **140.00** |
| 3 | Square tube | 1020 carbon steel, 35×35×2 mm, 2 pieces of 527 mm | 2 | ~20 |

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

## Machine Shop / Turner (~R$ 160)

| # | Item | Specification | Qty | Est. (R$) |
|---|------|--------------|:---:|----------:|
| 4 | Turned foot piece with collar | Carbon steel or stainless, Ø60 mm bar stock | 4 | ~160 |

**Part dimensions (bottom to top):**

| Section | Dimension |
|---------|-----------|
| Rubber | Ø60 mm × 1 mm neoprene (glued after machining) |
| Base | Ø60 mm × 8 mm |
| Chamfer | Ø60→Ø20, 6 mm height (~17°) |
| Collar | Ø20 mm × 5 mm (mechanical stop) |
| Thread | M12×1.75, Ø12 mm, 32 mm length |
| **Total height** | **52 mm** |

**Bring PDF:** `hardware/cad/fab_foot_piece.pdf`

---

## Metalwork / Machining (~R$ 20)

| # | Item | Specification | Qty | Est. (R$) |
|---|------|--------------|:---:|----------:|
| 5 | Steel shim | Carbon steel, 56×32 mm, 2 mm thick, 2 through holes Ø11 mm, 25 mm center-to-center | 4 | ~20 |

**Bring PDF:** `hardware/cad/fab_shim.pdf`

---

## Fasteners / Hardware (~R$ 50)

| # | Item | Specification | Qty | Est. (R$) |
|---|------|--------------|:---:|----------:|
| 6 | Flat-head Allen bolt | M10×50, DIN 7991 (countersunk/conical) | 8 | ~20 |
| 7 | M10 hex nut | DIN 934 (standard) or DIN 439 (thin) | 8 | ~5 |
| 8 | M10 flat washer | DIN 125 | 8 | ~5 |
| 9 | HSS metal drill bit | Ø11 mm | 1 | ~10 |
| 10 | 90° conical countersink | For M10, diameter Ø20 mm | 1 | ~10 |

---

## Materials and Consumables (~R$ 45)

| # | Item | Specification | Qty | Est. (R$) |
|---|------|--------------|:---:|----------:|
| 11 | Structural epoxy adhesive | Araldite Professional 24 ml (or Loctite EA, Devcon equiv.) | 1 | ~25 |
| 12 | Neoprene rubber | Ø60 mm × 1 mm disc (cut from sheet if needed) | 4 | ~10 |
| 13 | Metal sandpaper | 80 grit (surface preparation for bonding) | 2 | ~5 |
| 14 | Isopropyl alcohol | Degrease surfaces before bonding | 1 | ~5 |

---

## Summary by Supplier

| Supplier | Items | Subtotal | Status |
|----------|:-----:|----------:|--------|
| Casa dos Metais (Al plates) | 1–2 | **R$ 550** | Quoted |
| Metal supplier (cutting + tubes) | 3 + finishing 1–2 | ~R$ 50 | To estimate |
| Turner | 4 | ~R$ 160 | To estimate |
| Metalwork shop | 5 | ~R$ 20 | To estimate |
| Fastener shop | 6–10 | ~R$ 50 | To estimate |
| Materials | 11–14 | ~R$ 45 | To estimate |
| **Total** | **14 items** | **~R$ 875** | |

---

## Purchase Checklist

- [ ] Casa dos Metais — close purchase of 2 Al plates (R$ 550)
- [ ] Metal supplier — corner cutting (R30 + chamfer), drilling if possible, steel tubes (bring 3 PDFs)
- [ ] Turner — 4 foot pieces (bring 1 PDF)
- [ ] Metalwork shop — 4 steel shims (bring 1 PDF)
- [ ] Fastener shop — M10×50 DIN 7991 bolts + nuts + washers + drill bit + countersink
- [ ] Materials — epoxy + rubber + sandpaper + alcohol

> **⚠️ Before purchasing**
>
> 1. Wait for load cells to arrive (AliExpress)
> 2. Assemble 1 test corner to confirm the gap between plates
> 3. Steel tube: 35×35×2 mm (preferred) or 30×30×2 mm based on measured gap
> 4. Confirm M10×50 bolt length in actual stack assembly
