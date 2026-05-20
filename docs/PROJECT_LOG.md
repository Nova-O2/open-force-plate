# Project Log — Nova O2 Force Platform

Chronological project record. Most recent entry at the top.

For technical specs: [COMPONENT_SPECS.md](./COMPONENT_SPECS.md) | For costs: [COMPONENTS_SELECTED.md](./COMPONENTS_SELECTED.md) | For roadmap: [DEVELOPMENT_PLAN.md](./DEVELOPMENT_PLAN.md)

---

## 2026-05-19 (tarde) — Bonding session 1: top plate + tubes (parcial — 2ª sessão pendente)

### Execução

- **Tubos cortados** em 2× 500 mm (corte feito antes da lixa para não re-lixar topos)
- **Prep das superfícies (lado bondado hoje):** tubos inox lixados P150 → P24 (faces que mateiam com chapa superior); chapa superior Al 5052-F lixada P24
- **Degrease:** acetona pura (álcool isopropílico indisponível — Tekbond aceita acetona como alternativa equivalente)
- **Roteamento de cabos:** decidido passar pelo canal entre os 2 tubos — sem furos nas barras (evita concentrador de tensão + fadiga)
- **Aplicação:** Araldite Profissional 2× 23 g misturado 1:1 → aplicado nas 2 faces (top plate + topo dos tubos) → assentado → carga aplicada
- **Clamping improvisado:** sacos de areia distribuídos sobre as linhas dos tubos + tábua de distribuição de carga em cima da chapa superior + cunhas laterais para restrição de slip durante a fase de baixa viscosidade
- **Cura:** 24 h em temperatura ambiente em curso

### Desvio do plano original (Rev 3.1 → bonding em 2 estágios)

- Plano original: bondar chapas superior + inferior na mesma sessão com 2× 23 g (≈ 46 g total)
- Realidade: 46 g cobriu só uma face — folga de 25% sobre 25-35 mL estimados foi otimista em prática
- Decisão: bonding em 2 estágios — top plate hoje, bottom plate em sessão futura com novo lote de Araldite
- Trade-off aceito: 2 sessões + R$ 62 adicionais (compra) vs. risco de underfill da junta

### Pendente (próxima sessão)

- Comprar **mais 2× 23 g Araldite Profissional** (~R$ 62, Real Fortaleza Hidráulica)
- **Re-prep das faces remanescentes:**
  - Tubos: face oposta (que mateia com chapa inferior) — re-lixar P24 (Cr₂O₃ vai re-passivar até lá)
  - Chapa inferior Al 5052-F: prep nova P24 (não foi tocada hoje)
- Degrease acetona + aplicação + assentamento + clamping 24 h
- Apenas então: medir altura real da seção caixão + cotar 8 shims inox 304 (AL Usinagem) + checar entrega ML hardware

### Não atualizado nesta entrada (será atualizado quando a 2ª sessão fechar)

- README.md (EN + PT) — Status, cost breakdown, pending list
- docs/SHOPPING_LIST.md — total spent, item Araldite quantidade
- docs/COMPONENTS_SELECTED.md — quantidade real de Araldite
- 00-core/priorities.md — linha force-plate

Cascade write-through será feito de uma vez no fechamento da 2ª sessão (decisão Aldo, evita atualizar 2 vezes).

---

## 2026-05-19 (manhã) — Structural epoxy acquired (Araldite Professional)

- **Real Fortaleza Hidráulica Industrial** (same supplier as the Rev 3.1 inox 304 tube), Praça Independência 107, São João, Jacareí-SP
- **Araldite Profissional bicomponente** (Tekbond BRAP000), 23 g bisnaga — **2 unidades × R$ 31,00 = R$ 62,00**
- Estimate was ~R$ 50 → actual R$ 62 (+R$ 12 / +24%): single-supplier convenience over hunting hardware stores
- Unblocks bonding step (chapas + tubos inox 304 com epóxi estrutural, 24 h cura) once tube is cut into 2× 500 mm

### Pending (next steps)

- Cut tube into 2× 500 mm
- Buy remaining consumables (P40–P60 sandpaper, isopropyl alcohol, bar clamps)
- Bond plates + tubes with structural epoxy (24 h cure under clamping)
- Measure bonded box section height empirically → quote 8 inox 304 shims (AL Usinagem)
- Test-fit single corner → first calibration → promote `v3.1.0-rc1` → `v3.1.0`

---

## 2026-05-18 — Rev 3.1: stainless steel 304 structural tube acquired

### Tube purchased

- **Real Fortaleza Hidráulica Industrial** (D.A. Coutinho & Cia Ltda), Praça Independência 107, São João, Jacareí-SP
- TUBO QUADRADO 304 35×35×1,50 mm — 1,00 m — **R$ 103,67** (cartão de crédito, NFC-e nº 3014, 2026-05-18 13:22)
- Cut plan: 1 m bar → 2 pieces of 500 mm

### Spec deviations from Rev 3.0 (all validated, accepted as Rev 3.1)

1. **Material:** 1020 carbon steel → **stainless steel 304** — upgrade. Galvanic compatibility with Al 5052-F, no anti-corrosion coating needed. Completes the "inox 304 throughout" rule from Rev 3.0 (the tube was the last carbon-steel exception).
2. **Wall:** 2 mm → **1.5 mm** — the off-the-shelf stainless square tube. Transformed inertia recomputed: I_tr 1,305,342 → 1,234,842 mm⁴ (−5%). DJ 5× deflection 0.143 → 0.151 mm; structural FS 5.9 → 5.5; bond τ 0.95 → 0.98 MPa (FS ≈ 14–16×). All STRUCTURAL_ANALYSIS §9 acceptance criteria still met.
3. **Length:** 527 mm → **500 mm** (2 pieces from a 1 m bar) — covers the 475 mm support span with ~12.5 mm cantilever each side.

### Adhesive decision

- **Araldite Professional 90 min** (Tekbond, code BRAP000) selected for the MVP prototype — 2× 23 g bisnaga (≈ 42 mL, 25% headroom over the 25–35 mL effective need).
- On stainless, ambient cure: ~14–16 MPa shear → bond FS ≈ 14–16×. Design is dominated by stiffness, not bond strength.
- DP460 (≥ 20 MPa, FS > 20×) noted as the upgrade path for a continuously-used production v2 — overkill for the prototype.
- Surface prep: P40–P60 grit (coarse — stainless 304 passive Cr₂O₃ layer; P80 too fine).

### Documentation

- Transformed-section recalculation done by hand — the CAD scripts (`hardware/cad/*.py`) remain Rev 1.0 archaeological: they never implemented the composite transformed section, so `STRUCTURAL_ANALYSIS.md` §7 is the analysis SSOT. Recompute verified by reproducing the Rev 2.0 baseline.
- Cascade: STRUCTURAL_ANALYSIS, COMPONENT_SPECS, COMPONENTS_SELECTED, SHOPPING_LIST, README (EN+PT), DEVELOPMENT_PLAN updated to Rev 3.1.

### Pending (next steps)

- Buy Araldite Professional (2× 23 g) + consumables (P40–P60 sandpaper, isopropyl alcohol, bar clamps)
- Cut tube into 2× 500 mm
- Bond plates + tubes with structural epoxy (24 h cure under clamping)
- Measure bonded box section height empirically → quote 8 inox 304 shims (AL Usinagem)
- Test-fit single corner → first calibration → promote `v3.1.0-rc1` → `v3.1.0`

---

## 2026-05-08 — Rev 3.0 trigger: components received + fastening redesign

### Components received from AL Usinagem (machine shop)

- 4× turned foot pieces (M12 thread + collar + base + rubber pad)
  - **Spec deviation noted:** turned bar Ø55 mm (was specified Ø60 mm in Rev 2.0) — machine shop preference for available material stock
  - **Spec addition noted:** base vertical wall (Ø55 mm cylindrical surface) knurled (recartilhado) — facilitates operator grip when threading the foot piece M12 into the load cell
- 4× aluminum plates (top + bottom, both Al 5052-F) — drilled (8× Ø11 mm thru-holes each, with countersinking on top plate) + perimeter chamfer
  - **Acabamento (chamfer) details:**
    - Top plate (6.35 mm): 45° × 2.12 mm chamfer on **both faces** (1/3 of thickness)
    - Bottom plate (3 mm): 45° × 1.5 mm chamfer on **bottom face only** (1/2 of thickness)
  - Documented from AL Usinagem hand-sketch (lateral cross-section view)

### Costs (AL Usinagem)

- Foot pieces machining: R$ 1,120 (R$ 280 each × 4)
- Plate finishing (drilling + chamfer): R$ 360
- **Subtotal AL Usinagem (received): R$ 1,480**

### Hardware purchased today (MercadoLivre)

- M10×60 DIN 7991 inox 304 (kit 10 un) — **MIXPARAFUSOS** — R$ 76,05 (frete grátis)
- M10 Parlock all-metal locknut inox 304 (2× kit 10 un) — **EMAIFIX** — R$ 37,14 (16% off, frete grátis)
- M10 plain washer inox A2/304 (2× kit 10 un) — **USINIK** (loja oficial) — R$ 23,00 (frete grátis)
- **Subtotal ML hardware: R$ 136,19** — awaiting delivery

### Design decisions (this session) → trigger Rev 3.0

- Switch fastening from class 8.8 carbon steel to **inox 304 throughout** (parafuso + porca + arruela + shim) for galvanic compatibility with Al 5052-F plates and reusable anti-vibration locking (Parlock)
- **Add 4 bottom shims** (mirror configuration: 4 top + 4 bottom = 8 total). Bearing FS analysis: direct nut-on-aluminum (without bottom shim) gives FS ≈ 1.05 → unsafe; mirror shim brings FS ≈ 11
- Bolt length 50 → 60 mm to accommodate added bottom shim in stack (top plate 6.35 + top shim 1.5 + cell 32 + bottom shim 1.5 + bottom plate 3 = 44.35 mm + nut + washer)
- Shim thickness 2 → 1.5 mm nominal (final TBD empirical — see `COMPONENT_SPECS.md` §2.3.1 process gate)
- Torque target reduced 50–60 → 20–25 N·m (lower preload of A2-70 vs cl 8.8) + anti-seize on DIN 7991 cone face
- Discarded purchase: parafuso M10×40 DIN 7991 (Belenus, LUTEC) — incorrect length (would not reach nut after stack)

### Pending (next steps — see Rev 3.0 plan)

- Steel tubes 35×35×2 mm 1020 carbon — confirm arrival + dimensions with caliper
- Bond plates+tubes with structural epoxy (24 h cure)
- Measure bonded box section height + cell H actual at 4 corner positions
- Quote 8 new shims (inox 304, thickness from measurement) — AL Usinagem
- Hardware ML delivery
- Test-fit single corner before mass assembly (torque 20–25 N·m, no visible Al deformation)
- First calibration → triggers `v3.0.0-rc1` → `v3.0.0` final tag promotion

---

## 2026-04-25 — AL Usinagem kickoff: measurements verified, machining started

- Meeting with AL Usinagem (machine shop) — measurement check on aluminum plates and discussion of fabrication scope
- Measurements confirmed against fabrication PDFs (`hardware/cad/fab_top_plate.pdf`, `fab_bottom_plate.pdf`, `fab_foot_piece.pdf`)
- Machining started: top + bottom plates (corner cutting R30 / 15×15 chamfer + Ø11 mm drilling + Ø20 countersinking) and 4× turned foot bolts with collar
- Steel shims (4×) and steel tubes (35×35×2 mm box section) still to be sourced — pending gap measurement after first corner assembled

## 2026-04-23 — Load cells received

- 4× DYX-301 500 kg shear-beam load cells received, all units intact (no damage)
- Last AliExpress shipment closed — all components now in hand
- Unblocks: turned foot machining (measurements can be verified against actual cell threads/dimensions)

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
