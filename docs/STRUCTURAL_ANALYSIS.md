# Calculation Report — Structural Analysis of the Force Platform

**Date:** 2026-04-04
**Revision:** 1.0
**Author:** Aldo Seffrin + Claude Code (assisted analysis)

---

## 1. Objective

Verify the structural integrity of the force platform's top plate under operating loads (athletes standing, CMJ and DJ jumps), determining maximum deflection, stress, and safety factor. Define the necessary structural reinforcement.

---

## 2. Input Data

### 2.1 Materials

#### Plates — Aluminum 5052-F

| Property | Value |
|----------|-------|
| Modulus of elasticity (E) | 70,300 MPa |
| Yield strength (σ_y) | 90 MPa |
| Poisson's ratio (ν) | 0.33 |
| Density (ρ) | 2,680 kg/m³ |

> **ℹ️ Material change (Rev. 2.0)**
>
> Original alloy: 6061-T6 (σ_y = 276 MPa). Replaced by 5052-F due to local availability. The modulus of elasticity is practically the same (~70 GPa), so **deflection does not change**. The reduction in yield strength is offset by the structural margin of the box section (FS > 4 in all scenarios).

#### Reinforcement tubes — 1020 carbon steel

| Property | Value |
|----------|-------|
| Modulus of elasticity (E) | 200,000 MPa |
| Yield strength (σ_y) | 250 MPa |
| Density (ρ) | 7,850 kg/m³ |
| Modular ratio (n = E_steel/E_al) | 2.845 |

> **ℹ️ Material change (Rev. 2.0)**
>
> Original tubes: aluminum 35×35×2 mm. Replaced by carbon steel due to local availability. Square aluminum tubes are difficult to find in the regional market; steel is standard in any metal supply shop. The substitution adds +1.4 kg to the total weight but **increases box section stiffness by ~23%**.

### 2.2 Geometry

| Component | Dimensions |
|-----------|------------|
| Top plate | 600 × 500 × 6.35 mm (1/4"), Al 5052-F, corners R30 |
| Bottom plate | 527 × 396 × 3 mm, Al 5052-F, chamfered corners 15×15 |
| Reinforcement tube | 35×35 × 2 mm, 1020 carbon steel, 527 mm length, ×2 |
| Holes | Ø11 mm (M10 DIN 7991), countersunk Ø20 on top plate |

### 2.3 Supports (Load Cells)

Centers of hole pairs (reference: bottom-left corner of top plate):

| Cell | X (mm) | Y (mm) |
|:----:|:------:|:------:|
| C1 (top-left) | 62.5 | 417.1 |
| C2 (top-right) | 537.5 | 417.1 |
| C3 (bottom-left) | 62.5 | 83.0 |
| C4 (bottom-right) | 537.5 | 83.0 |

**Span between supports:**
- X-axis: 537.5 − 62.5 = **475.0 mm**
- Y-axis: 417.1 − 83.0 = **334.1 mm**

### 2.4 Load Scenarios

| Scenario | Mass (kg) | Multiplier | Force (N) |
|----------|:---------:|:----------:|:---------:|
| Light athlete — standing | 70 | 1.0× | 687 |
| Average athlete — standing | 85 | 1.0× | 834 |
| Heavy athlete — standing | 120 | 1.0× | 1,177 |
| Average athlete — CMJ peak | 85 | 3.0× | 2,502 |
| Heavy athlete — CMJ peak | 120 | 3.0× | 3,532 |
| Heavy athlete — DJ peak | 120 | 5.0× | 5,886 |
| Heavy athlete — DJ extreme | 120 | 7.0× | 8,240 |

**Critical design scenario:** DJ 5×BW with 120 kg athlete → **P = 5,886 N**

---

## 3. Calculation Model

### 3.1 Adopted model

Kirchhoff rectangular plate on 4 point supports, with concentrated load at center (worst case). Solution by Navier double Fourier series for simply supported plate, with 1.8× correction factor for point supports (more flexible than edge supports).

### 3.2 Plate flexural rigidity

$$D = \frac{E \cdot t^3}{12 \cdot (1 - \nu^2)}$$

For t = 6.35 mm (Al 5052-F):

$$D = \frac{70,300 \times 6.35^3}{12 \times (1 - 0.33^2)} = \frac{70,300 \times 256.0}{12 \times 0.8911} = \frac{17,997,000}{10.693} = 1,683,000 \text{ N·mm}$$

> **📝 Note**
>
> D increased ~21% vs. original design (1,392,000 N·mm with 6061-T6 6 mm) — combined effect of slightly higher E and 6.35 mm thickness.

### 3.3 Deflection — Navier Series (plate center)

$$w_{max} = \frac{4P}{ab\pi^4 D} \sum_{m=1,3,5...} \sum_{n=1,3,5...} \frac{1}{\left[\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2\right]^2}$$

With a = 475 mm, b = 334 mm, convergence with 80 terms.

Point support correction factor: **×1.8** (conservative).

---

## 4. Results — Unreinforced Plate (6.35 mm, Al 5052-F)

| Scenario | P (N) | Deflection (mm) | Stress (MPa) | FS |
|----------|:-----:|:---------------:|:------------:|:--:|
| 120 kg standing | 1,177 | 2.11 | 168.0 | 0.5 |
| 85 kg CMJ 3× | 2,502 | 4.48 | 357.0 | 0.3 |
| 120 kg DJ 5× | 5,886 | 10.52 | 840.0 | 0.1 |

> **🔴 FAILURE**
>
> The 6.35 mm plate without reinforcement shows **10.5 mm** deflection and stress **9.3× above yield** in the DJ scenario. Even worse than 6061-T6 in terms of FS, since the reduction in σ_y (90 MPa) outweighs the thickness gain. Structural reinforcement is mandatory.

---

## 5. Alternative Materials Study

Comparative evaluation for the critical scenario (DJ 5×BW, 120 kg):

| Material | Thickness | Plate weight | Est. cost | Deflection | FS |
|----------|:---------:|:------------:|:---------:|:----------:|:--:|
| Al 5052-F | 6.35 mm | 5.11 kg | R$ 150 | 10.52 mm | 0.1 |
| Al 6061-T6 | 6 mm | 4.86 kg | R$ 194 | 12.72 mm | 0.3 |
| Al 6061-T6 | 15 mm | 12.15 kg | R$ 486 | 0.81 mm | 2.1 |
| Steel 1020 | 10 mm | 23.55 kg | R$ 283 | 0.97 mm | 1.2 |
| Steel 1045 | 10 mm | 23.55 kg | R$ 353 | 0.95 mm | 1.9 |
| Steel 1045 | 12 mm | 28.26 kg | R$ 424 | 0.55 mm | 2.7 |
| Stainless 304 | 12 mm | 28.80 kg | R$ 1,008 | 0.58 mm | 1.1 |

**Conclusion:** Single plate (unreinforced) requires high thickness — 15 mm in aluminum or 10–12 mm in steel. The 5052-F alloy has an even lower FS than 6061-T6 as a standalone plate. Alternative: structural reinforcement (box section).

---

## 6. Structural Reinforcement Analysis

### 6.1 Options evaluated

| Option | Concept | Add. weight | Cost | DJ 5× deflection |
|--------|---------|:-----------:|:----:|:----------------:|
| Al ribs 3×50×6 mm | Bars bonded under plate | +1.5 kg | ~R$ 78 | 0.27 mm |
| Steel tube frame 30×30 | Welded frame | +6.2 kg | ~R$ 124 | 0.43 mm |
| Box section 2 Al tubes | Al plates + Al tubes bonded | +0.75 kg | ~R$ 50 | 0.18 mm |
| **Box section 2 steel tubes** | **Al plates + steel tubes bonded** | **+2.18 kg** | **~R$ 25** | **0.14 mm** |

> **ℹ️ Design evolution (Rev. 2.0)**
>
> The original design used 35×35×2 mm aluminum tubes — the lightest solution (+0.75 kg). In practice, square aluminum tubes are difficult to find in the Brazilian regional market. Steel tubes are an off-the-shelf product at any metal supply shop. The substitution adds 1.4 kg but **increases stiffness by 23%** and **reduces cost** (steel is cheaper than aluminum per meter).

### 6.2 Adopted solution — Box section (steel tubes)

The two 5052-F aluminum plates (top 6.35 mm + bottom 3 mm) act as flanges of a box beam, connected by **2 square 1020 carbon steel tubes** bonded with structural epoxy.

```
╔══════════════════════════╗  ← top plate Al 5052-F 6.35 mm (flange)
║    ┌────┐        ┌────┐  ║
║    │tube│        │tube│  ║  ← 2 steel tubes 1020 35×35×2 mm (web)
║    │ 1  │        │ 2  │  ║
║    └────┘        └────┘  ║
╚══════════════════════════╝  ← bottom plate Al 5052-F 3 mm (flange)
```

**Tube positions (ref. top plate):**
- Tube 1: Y = 194 mm (longitudinal, X-axis)
- Tube 2: Y = 306 mm (longitudinal, X-axis)
- Length: 527 mm (= bottom plate width)
- Minimum clearance to load cells: ~100 mm (no interference)

---

## 7. Box Section Calculation

### 7.1 Method — Transformed section

Since the box section combines two materials (aluminum plates + steel tubes), the **transformed section method** is used: steel areas are converted to equivalent aluminum areas using the modular ratio n = E_steel / E_al = 200,000 / 70,300 = **2.845**.

> **ℹ️ Calculation evolution (Rev. 2.0)**
>
> In Rev. 1.0 (all-aluminum section), the calculation was straightforward with a single material. The transformed section is required when mixing materials — standard technique in composite structures (e.g., reinforced concrete, steel-timber composite beams).

### 7.2 Composite section geometry (transformed to aluminum)

Reference: bottom of bottom plate (y = 0)
Total height: 3 + 35 + 6.35 = **44.35 mm**

| Component | Material | Real area (mm²) | n | Transf. area (mm²) | Centroid y (mm) |
|-----------|----------|:---------------:|:---:|:------------------:|:---------------:|
| Bottom plate (300×3 mm) | Al 5052-F | 900 | 1.0 | 900 | 1.50 |
| Tube 1 (35×35×2 mm) | Steel 1020 | 264 | 2.845 | 751 | 20.50 |
| Tube 2 (35×35×2 mm) | Steel 1020 | 264 | 2.845 | 751 | 20.50 |
| Top plate (300×6.35 mm) | Al 5052-F | 1,905 | 1.0 | 1,905 | 41.18 |
| **Total** | — | **3,333** | — | **4,307** | — |

**Effective width adopted:** 300 mm (conservative — plate effective width)

### 7.3 Centroid of transformed section

$$\bar{y} = \frac{\sum A_{tr,i} \cdot y_i}{\sum A_{tr,i}} = \frac{900 \times 1.5 + 2 \times 751 \times 20.5 + 1905 \times 41.18}{4307} = \frac{110,584}{4,307} = 25.7 \text{ mm}$$

### 7.4 Transformed moment of inertia (Steiner's theorem)

| Component | Own transf. I (mm⁴) | A_tr·d² (mm⁴) | Total I (mm⁴) |
|-----------|:-------------------:|:--------------:|:-------------:|
| Al bottom plate | 675 | 526,203 | 526,878 |
| Steel tube 1 (×n) | 136,822 | 20,076 | 156,898 |
| Steel tube 2 (×n) | 136,822 | 20,076 | 156,898 |
| Al top plate | 6,401 | 458,267 | 464,668 |
| **TOTAL** | — | — | **1,305,342** |

**Comparison Rev. 1.0 → Rev. 2.0:**

| Version | I_total (mm⁴) | EI (×10⁹ N·mm²) | Gain |
|---------|:-------------:|:----------------:|:----:|
| Rev. 1.0 — all Al, 6 mm | 1,062,162 | 73.2 | reference |
| **Rev. 2.0 — Al 5052-F 6.35 mm + steel** | **1,305,342** | **91.8** | **+25%** |

**Stiffness gain vs. plate alone:** I_box / I_plate_6.35mm = 1,305,342 / 6,401×(300/300) ≈ **~150×**

### 7.5 Results — Box section Rev. 2.0 (Al 5052-F + steel tubes)

| Scenario | P (N) | Deflection (mm) | Al stress (MPa) | FS (σ_y = 90 MPa) |
|----------|:-----:|:---------------:|:---------------:|:-----------------:|
| 70 kg standing | 687 | 0.017 | 1.7 | 53 |
| 85 kg standing | 834 | 0.020 | 2.2 | 41 |
| 120 kg standing | 1,177 | 0.029 | 3.1 | 29 |
| 85 kg CMJ 3× | 2,502 | 0.061 | 6.5 | 14 |
| 120 kg CMJ 3× | 3,532 | 0.086 | 9.2 | 9.8 |
| **120 kg DJ 5×** | **5,886** | **0.143** | **15.3** | **5.9** |
| 120 kg DJ 7× (extreme) | 8,240 | 0.200 | 21.4 | 4.2 |

> **ℹ️ Info**
>
> Maximum deflection < 0.2 mm in all scenarios, including extreme DJ. FS > 4 in all conditions — even with the 5052-F alloy (σ_y = 90 MPa), the box section provides ample safety margin.

**Comparison Rev. 1.0 → Rev. 2.0 (critical scenario DJ 5×, 120 kg):**

| Parameter | Rev. 1.0 (Al 6061-T6, Al tubes) | Rev. 2.0 (Al 5052-F, steel tubes) |
|-----------|:--------------------------------:|:----------------------------------:|
| Deflection | 0.180 mm | **0.143 mm** (−21%) |
| Al stress | 17.5 MPa | **15.3 MPa** (−13%) |
| FS | 15.7 | **5.9** (lower σ_y) |
| Tube weight | 0.75 kg | **2.18 kg** (+1.4 kg) |

### 7.6 Sensitivity to tube size

| Tube | Transf. I (mm⁴) | DJ 5× deflection | Difference |
|------|:---------------:|:----------------:|:----------:|
| Steel 35×35×2 mm | 1,305,342 | 0.143 mm | reference |
| Steel 30×30×2 mm | ~1,240,000 | ~0.150 mm | +5% |

Negligible difference — both sizes comply with comfortable margin. Prefer 35×35 if available.

---

## 8. Bond Verification

### 8.1 Shear at tube-plate interface (steel→aluminum)

| Parameter | Value |
|-----------|-------|
| Maximum shear (V = P/2) | 2,943 N |
| Transformed first moment of area (Q_top) | 29,537 mm³ |
| Shear flow (q = VQ/I_tr) | 66.6 N/mm |
| Bond width (2 tubes × 35 mm) | 70 mm |
| Adhesive stress (τ = q/b) | **0.95 MPa** |
| Structural epoxy strength | 20–30 MPa |
| **Bond safety factor** | **> 21** |

> **📝 Note**
>
> The steel↔aluminum interface via epoxy is well established in engineering practice. Steel has natural roughness that promotes mechanical adhesion. Preparation: sand both surfaces (80 grit), degrease with isopropyl alcohol, apply epoxy, and cure 24 h under clamp pressure.

### 8.2 Adhesive specification

- Type: two-part structural epoxy (Araldite Professional, Loctite EA 9461, or equivalent)
- Shear strength: ≥ 20 MPa
- Preparation: sand surfaces (80 grit), degrease (isopropyl alcohol)
- Cure: 24 h under pressure (clamps)

---

## 8.3 Bearing Stress Verification at Supports

Verification of localized bearing at contact points between plates, steel shims, and load cells — a failure mode distinct from global bending.

### 8.3.1 Load path

```
Athlete's foot
    ↓
Top plate Al 6 mm
    ↓ (face-to-face contact)
Steel shim 56×32×2 mm
    ↓ (face-to-face contact)
Load cell top (boss M10)
    ↓
DYX-301 load cell body
    ↓
Bottom shim + bottom plate
```

The vertical compressive load is transferred by **direct face-to-face contact** between plate→shim→cell. The M10 DIN 7991 bolt **does not carry the jump force** — it only keeps the sandwich together and resists lateral components (horizontal GRF).

### 8.3.2 Bearing stress in aluminum (under shim)

| Parameter | Value |
|-----------|-------|
| Force per cell (DJ 5×BW, 120 kg) | 1,472 N |
| Shim area (56 × 32 mm) | 1,792 mm² |
| **Contact pressure on Al** | **0.82 MPa** |
| Al 5052-F yield strength (σ_y) | 90 MPa |
| Al 5052-F bearing yield (~1.5× σ_y) | ~135 MPa |
| **Safety factor** | **165×** |

**Extreme scenario (DJ 7×BW, 120 kg):** 2,060 N/cell → 1.15 MPa → FS = 117×.

### 8.3.3 Function of the steel shims

The 56×32×2 mm steel shims were specifically dimensioned for this failure mode:

1. **Load spreading** — distribute the force from the load cell boss (~Ø25–30 mm, ~600 mm²) over 1,792 mm², reducing pressure by 3×
2. **Aluminum protection** — steel↔aluminum interface prevents marking/creep over thousands of jump cycles
3. **Coplanarity** — absorbs small flatness imperfections, preventing point contact

### 8.3.4 Lateral shear on bolt (horizontal GRF)

| Parameter | Value |
|-----------|-------|
| Horizontal GRF (~10–15% of vertical) | ~220 N/cell |
| Bolts per cell | 2 |
| Shear per bolt | 110 N |
| M10 cl. 8.8 capacity (A_s × 0.6 × σ_ut) | ~27,800 N |
| **Safety factor** | **> 250** |

### 8.3.5 Fatigue

Cyclic stress at steel shim: 0.82 MPa, well below the fatigue limit of carbon steel (150–200 MPa) → **infinite life** (> 10⁶ cycles).

### 8.3.6 Acceptance criteria (bearing)

| Criterion | Limit | Result | Status |
|-----------|:-----:|:------:|:------:|
| Al pressure under shim (DJ 5×) | < 100 MPa | 0.82 MPa | ✅ |
| Bearing FS Al 5052-F (DJ 7×) | ≥ 3.0 | 165× | ✅ |
| Bolt shear FS | ≥ 3.0 | > 250 | ✅ |
| Shim fatigue (10⁶ cycles) | < 150 MPa | 0.82 MPa | ✅ |

---

## 9. Acceptance Criteria

| Criterion | Limit | Result | Status |
|-----------|:-----:|:------:|:------:|
| Maximum deflection (DJ 5×BW) | < 0.5 mm | 0.14 mm | ✅ |
| Maximum deflection (CMJ 3×BW) | < 0.2 mm | 0.06 mm | ✅ |
| Safety factor (DJ 5×) | ≥ 2.0 | 5.9 | ✅ |
| Bond FS (DJ 5×) | ≥ 3.0 | > 21 | ✅ |

---

## 10. Design Decision

### Problem
The 6 mm aluminum top plate without reinforcement deflects 12.7 mm under DJ load (120 kg, 5×BW) — unacceptable for a force platform (measurement accuracy).

### Alternatives evaluated
1. Increase thickness (15 mm Al or 10 mm steel) — heavy and/or expensive
2. Bonded ribs — effective but less elegant
3. Steel tube frame — good but heavy (+6 kg) and requires welding
4. **Box section with square tubes** — best cost-weight-stiffness ratio

### Adopted solution (Rev. 2.0)
2 square **1020 carbon steel** tubes (35×35×2 mm) bonded with structural epoxy between the two 5052-F aluminum plates, creating a box section with I_transformed = 1,305,342 mm⁴ (~150× the plate alone).

> **ℹ️ Design evolution**
>
> Rev. 1.0: aluminum tubes (I = 1,062,000 mm⁴, +0.75 kg, ~R$50).
> Rev. 2.0: steel tubes (I_tr = 1,305,000 mm⁴, +2.18 kg, ~R$25). Driven by local availability — aluminum tubes are difficult to find in the regional market, while steel is an off-the-shelf product.

### Impact (Rev. 2.0)

| Parameter | Unreinforced | With reinforcement Rev. 2.0 | Improvement |
|-----------|:-----------:|:---------------------------:|:-----------:|
| DJ 5× deflection | 10.52 mm | 0.14 mm | **75×** |
| Structural FS (5052-F) | 0.1 | 5.9 | **59×** |
| Additional weight | — | +2.18 kg | — |
| Additional cost | — | ~R$ 25 | — |

---

## 11. Model Limitations

1. **Analytical model** — Navier series with empirical correction factor (1.8×) for point supports. For definitive validation, FEA or physical testing is recommended.
2. **Point load** — the model assumes a concentrated load at the center (worst case). In practice, the athlete's foot distributes the load over ~200–300 cm², reducing actual deflection.
3. **Effective width** — adopted as 300 mm (conservative). The actual contribution of the plates may be greater.
4. **Ideal bond** — assumes perfect shear transfer through the adhesive. Surface preparation is critical, especially at the steel↔aluminum interface.
5. **Dynamic effects not considered** — impact loads (DJ) are transient and system inertia attenuates peaks.
6. **Galvanic corrosion** — steel↔aluminum contact can cause galvanic corrosion in humid environments. Mitigation: the epoxy layer between surfaces acts as an insulator. For indoor lab/gym use, risk is negligible.

---

## 12. References

- Timoshenko, S. P., Woinowsky-Krieger, S. (1959). *Theory of Plates and Shells*, 2nd Ed. McGraw-Hill.
- Young, W. C., Budynas, R. G. (2002). *Roark's Formulas for Stress and Strain*, 7th Ed. McGraw-Hill.
- Calculation scripts: `hardware/cad/structural_analysis.py`, `hardware/cad/material_comparison.py`, `hardware/cad/reinforcement_analysis.py`, `hardware/cad/box_section_analysis.py`

---

## 13. Revision History

| Rev. | Date | Description |
|:----:|:----:|-------------|
| 1.0 | 2026-04-04 | Full analysis: unreinforced plate, material comparison, box section solution (Al 6061-T6, Al tubes) |
| 1.1 | 2026-04-04 | Added Section 8.3 — bearing stress verification at supports (plate↔shim↔cell) |
| 2.0 | 2026-04-06 | Material update for local availability: Al 5052-F 6.35 mm plates (replaces 6061-T6 6 mm), 1020 steel tubes (replaces Al). Full recalculation with transformed section. All criteria met with comfortable margin (FS ≥ 4.2). |
