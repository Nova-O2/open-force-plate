# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (c) 2026 Nova O2

"""
Force Plate MVP — Material Comparison
Nova O2 Sport Science

Compara deflexao, tensao, peso e custo estimado para diferentes
materiais e espessuras na chapa superior.
"""

# NOTE: This script reflects the Rev 1.0 analysis (Al 6061-T6, 6mm top plate,
# aluminum tubes). The current design (Rev 2.0) uses Al 5052-F, 6.35mm top plate,
# and 1020 carbon steel tubes. Updated calculations are documented in
# docs/STRUCTURAL_ANALYSIS.md. Script update to Rev 2.0 values is planned.

import numpy as np

# =============================================================================
# GEOMETRIA
# =============================================================================
W, H = 600, 500          # Dimensoes da chapa (mm)
span_x = 475.0            # Vao entre apoios X (mm)
span_y = 334.1            # Vao entre apoios Y (mm)
POINT_SUPPORT_FACTOR = 1.8

# Carga de referencia: atleta 120 kg, DJ 5× BW
P_ref = 120 * 9.81 * 5   # 5886 N

# =============================================================================
# MATERIAIS
# =============================================================================
materials = [
    {
        'name': u'Aluminio 6061-T6',
        'short': 'Al 6061',
        'E': 68_900,         # MPa
        'sigma_y': 276,      # MPa
        'nu': 0.33,
        'rho': 2_700,        # kg/m³
        'cost_kg': 40,       # R$/kg (chapa cortada)
        'available': [4, 5, 6, 8, 10, 12, 15],
    },
    {
        'name': u'Aco carbono 1020 (laminado)',
        'short': u'Aco 1020',
        'E': 200_000,
        'sigma_y': 350,
        'nu': 0.30,
        'rho': 7_850,
        'cost_kg': 12,
        'available': [3, 4, 5, 6, 8, 10, 12],
    },
    {
        'name': u'Aco carbono 1045 (medio carbono)',
        'short': u'Aco 1045',
        'E': 205_000,
        'sigma_y': 530,
        'nu': 0.29,
        'rho': 7_850,
        'cost_kg': 15,
        'available': [3, 4, 5, 6, 8, 10, 12],
    },
    {
        'name': u'Aco inox 304',
        'short': 'Inox 304',
        'E': 193_000,
        'sigma_y': 215,
        'nu': 0.29,
        'rho': 8_000,
        'cost_kg': 35,
        'available': [3, 4, 5, 6, 8, 10, 12],
    },
    {
        'name': u'Aco inox 316',
        'short': 'Inox 316',
        'E': 193_000,
        'sigma_y': 290,
        'nu': 0.29,
        'rho': 8_000,
        'cost_kg': 45,
        'available': [3, 4, 5, 6, 8, 10],
    },
]


def plate_deflection(P, a, b, t, E, nu, n_terms=60):
    """Deflexao no centro de placa simplesmente apoiada com carga central."""
    D = E * t**3 / (12 * (1 - nu**2))
    w = 0.0
    for m in range(1, n_terms + 1, 2):
        for n in range(1, n_terms + 1, 2):
            alpha = (m * np.pi / a)**2 + (n * np.pi / b)**2
            Qmn = (4 * P / (a * b))  # sin(m*pi/2)*sin(n*pi/2) = 1 for odd m,n
            w += Qmn / (D * alpha**2)
    return abs(w) * POINT_SUPPORT_FACTOR


def plate_stress(P, a, b, t, E, nu, n_terms=60):
    """Tensao maxima de flexao no centro."""
    D = E * t**3 / (12 * (1 - nu**2))
    Mx = 0.0
    for m in range(1, n_terms + 1, 2):
        for n in range(1, n_terms + 1, 2):
            alpha = (m * np.pi / a)**2 + (n * np.pi / b)**2
            Qmn = (4 * P / (a * b))
            wmn = Qmn / (D * alpha**2)
            d2x = -wmn * (m * np.pi / a)**2
            d2y = -wmn * (n * np.pi / b)**2
            Mx += -D * (d2x + nu * d2y)
    sigma = 6 * abs(Mx) / t**2
    return sigma * POINT_SUPPORT_FACTOR


# =============================================================================
# ANALISE
# =============================================================================

print("=" * 90)
print("COMPARATIVO DE MATERIAIS — CHAPA SUPERIOR DA PLATAFORMA DE FORCA")
print(f"Carga de referencia: 120 kg atleta, DJ 5x BW = {P_ref:.0f} N")
print(f"Vao entre apoios: {span_x:.0f} x {span_y:.0f} mm | Chapa: {W} x {H} mm")
print("=" * 90)

for mat in materials:
    print(f"\n{'─' * 90}")
    print(f"  {mat['name']}")
    print(f"  E = {mat['E']:,} MPa | sigma_y = {mat['sigma_y']} MPa | "
          f"rho = {mat['rho']:,} kg/m3 | ~R${mat['cost_kg']}/kg")
    print(f"{'─' * 90}")
    print(f"  {'Esp.':>5}  {'Peso':>8}  {'Custo':>9}  {'Deflexao':>10}  "
          f"{'Tensao':>10}  {'FS':>5}  {'Status':<12}")

    for t in mat['available']:
        mass = (W * H * t * 1e-9) * mat['rho']
        cost = mass * mat['cost_kg']
        delta = plate_deflection(P_ref, span_x, span_y, t, mat['E'], mat['nu'])
        sigma = plate_stress(P_ref, span_x, span_y, t, mat['E'], mat['nu'])
        fs = mat['sigma_y'] / sigma if sigma > 0 else 999

        if delta <= 0.5 and fs >= 2.0:
            status = "IDEAL"
        elif delta <= 0.5 and fs >= 1.5:
            status = "BOM"
        elif delta <= 1.0 and fs >= 1.5:
            status = "ACEITAVEL"
        elif fs < 1.0:
            status = "FALHA"
        else:
            status = "INSUFICIENTE"

        print(f"  {t:>4}mm  {mass:>6.2f}kg  R${cost:>6.0f}  "
              f"{delta:>8.2f}mm  {sigma:>8.1f}MPa  {fs:>5.1f}  {status}")


# =============================================================================
# RESUMO — MELHORES OPCOES
# =============================================================================

print(f"\n{'=' * 90}")
print("MELHORES OPCOES (deflexao < 0.5mm E FS >= 2.0 no DJ 5x BW)")
print("=" * 90)

options = []
for mat in materials:
    for t in mat['available']:
        mass = (W * H * t * 1e-9) * mat['rho']
        cost = mass * mat['cost_kg']
        delta = plate_deflection(P_ref, span_x, span_y, t, mat['E'], mat['nu'])
        sigma = plate_stress(P_ref, span_x, span_y, t, mat['E'], mat['nu'])
        fs = mat['sigma_y'] / sigma if sigma > 0 else 999

        if delta <= 0.5 and fs >= 2.0:
            options.append((mat['short'], t, mass, cost, delta, sigma, fs))

options.sort(key=lambda x: x[3])  # ordenar por custo

if options:
    print(f"\n  {'Material':<14} {'Esp.':>5} {'Peso':>8} {'Custo':>9} "
          f"{'Deflexao':>10} {'Tensao':>10} {'FS':>5}")
    print(f"  {'─' * 76}")
    for mat_name, t, mass, cost, delta, sigma, fs in options:
        print(f"  {mat_name:<14} {t:>4}mm {mass:>6.2f}kg R${cost:>6.0f} "
              f"{delta:>8.2f}mm {sigma:>8.1f}MPa {fs:>5.1f}")
else:
    print("\n  Nenhuma opcao atende ambos os criterios nas espessuras testadas.")
    print("  Considerar espessuras maiores ou reforcos estruturais.")


# =============================================================================
# CENARIOS DE USO REAL (atleta 85kg CMJ — caso mais comum)
# =============================================================================

P_cmj = 85 * 9.81 * 3  # 85kg, CMJ 3× BW = 2502 N

print(f"\n{'=' * 90}")
print(f"CENARIO MAIS COMUM: atleta 85 kg, CMJ 3x BW = {P_cmj:.0f} N")
print("=" * 90)

options_cmj = []
for mat in materials:
    for t in mat['available']:
        mass = (W * H * t * 1e-9) * mat['rho']
        cost = mass * mat['cost_kg']
        delta = plate_deflection(P_cmj, span_x, span_y, t, mat['E'], mat['nu'])
        sigma = plate_stress(P_cmj, span_x, span_y, t, mat['E'], mat['nu'])
        fs = mat['sigma_y'] / sigma if sigma > 0 else 999

        if delta <= 0.5 and fs >= 2.0:
            options_cmj.append((mat['short'], t, mass, cost, delta, sigma, fs))

options_cmj.sort(key=lambda x: x[3])

if options_cmj:
    print(f"\n  {'Material':<14} {'Esp.':>5} {'Peso':>8} {'Custo':>9} "
          f"{'Deflexao':>10} {'Tensao':>10} {'FS':>5}")
    print(f"  {'─' * 76}")
    for mat_name, t, mass, cost, delta, sigma, fs in options_cmj:
        print(f"  {mat_name:<14} {t:>4}mm {mass:>6.2f}kg R${cost:>6.0f} "
              f"{delta:>8.2f}mm {sigma:>8.1f}MPa {fs:>5.1f}")

# =============================================================================
# COMPARATIVO DIRETO: mesma espessura 6mm
# =============================================================================

print(f"\n{'=' * 90}")
print("COMPARATIVO DIRETO — Todos os materiais a 6mm (espessura atual)")
print(f"Cenario: 120 kg DJ 5x BW ({P_ref:.0f} N)")
print("=" * 90)

t_fix = 6
print(f"\n  {'Material':<30} {'Peso':>8} {'Custo':>9} {'Deflexao':>10} "
      f"{'Tensao':>10} {'FS':>5}")
print(f"  {'─' * 78}")

for mat in materials:
    mass = (W * H * t_fix * 1e-9) * mat['rho']
    cost = mass * mat['cost_kg']
    delta = plate_deflection(P_ref, span_x, span_y, t_fix, mat['E'], mat['nu'])
    sigma = plate_stress(P_ref, span_x, span_y, t_fix, mat['E'], mat['nu'])
    fs = mat['sigma_y'] / sigma if sigma > 0 else 999
    print(f"  {mat['name']:<30} {mass:>6.2f}kg R${cost:>6.0f} "
          f"{delta:>8.2f}mm {sigma:>8.1f}MPa {fs:>5.1f}")
