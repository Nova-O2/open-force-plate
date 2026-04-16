"""
Plataforma de Forca MVP — Analise Estrutural
Nova O2 Ciencia do Esporte

Calcula deflexao e tensao na chapa superior sob diferentes cenarios de carga.
Modelo: placa retangular sobre 4 apoios pontuais (celulas de carga).

Referencias:
- Timoshenko, S. "Theory of Plates and Shells", 2nd Ed.
- Roark's Formulas for Stress and Strain, 8th Ed.
"""

import numpy as np

# =============================================================================
# MATERIAL — Aluminio 6061-T6
# =============================================================================
E = 68_900        # Modulo de elasticidade (MPa = N/mm²)
sigma_yield = 276  # Tensao de escoamento (MPa)
nu = 0.33          # Coeficiente de Poisson
rho_al = 2_700     # Densidade (kg/m³)

# =============================================================================
# GEOMETRIA DA CHAPA SUPERIOR
# =============================================================================
W = 600            # Largura (mm)
H = 500            # Comprimento (mm)
t = 6              # Espessura (mm)

# Posicoes dos apoios (centros dos pares de furos — aprox.)
# C1(sup-esq), C2(sup-dir), C3(inf-esq), C4(inf-dir)
supports = {
    'C1': ((56.7 + 68.3) / 2, (428.1 + 406.0) / 2),   # (62.5, 417.0)
    'C2': ((543.3 + 531.7) / 2, (428.1 + 406.0) / 2),  # (537.5, 417.0)
    'C3': ((56.7 + 68.3) / 2, (71.9 + 94.0) / 2),      # (62.5, 83.0)
    'C4': ((543.3 + 531.7) / 2, (71.9 + 94.0) / 2),    # (537.5, 83.0)
}

# Vao entre apoios
span_x = supports['C2'][0] - supports['C1'][0]  # 475 mm
span_y = supports['C1'][1] - supports['C3'][1]  # 334 mm

# Balanco (overhang) alem dos apoios
overhang_left = supports['C3'][0]                # 62.5 mm
overhang_right = W - supports['C4'][0]           # 62.5 mm
overhang_bottom = supports['C3'][1]              # 83.0 mm
overhang_top = H - supports['C1'][1]             # 83.0 mm

# =============================================================================
# CARGAS — Cenarios de uso
# =============================================================================
g = 9.81  # m/s²

scenarios = [
    ("Atleta leve (70 kg) — em pe",      70,  1.0),
    ("Atleta medio (85 kg) — em pe",      85,  1.0),
    ("Atleta pesado (120 kg) — em pe",   120,  1.0),
    ("Atleta pesado (120 kg) — CMJ pico", 120, 3.0),   # 3x BW tipico CMJ
    ("Atleta pesado (120 kg) — DJ pico",  120, 5.0),    # 5x BW tipico DJ
    ("Atleta pesado (120 kg) — DJ extremo", 120, 7.0),  # 7x BW pior caso
    ("Carga maxima (2000 kg)",           2000, 1.0),     # capacidade total
]

# =============================================================================
# PROPRIEDADES DA SECAO
# =============================================================================

# Rigidez flexural da placa (Kirchhoff)
D = E * t**3 / (12 * (1 - nu**2))

# Momento de inercia (para analise de viga, por unidade de largura)
I_per_mm = t**3 / 12  # mm⁴/mm

# Peso proprio da chapa
plate_mass = (W * H * t * 1e-9) * rho_al  # kg
plate_weight = plate_mass * g              # N

print("=" * 72)
print("ANALISE ESTRUTURAL — CHAPA SUPERIOR DA PLATAFORMA DE FORCA")
print("Nova O2 Ciencia do Esporte")
print("=" * 72)

print(f"\n--- PARAMETROS ---")
print(f"Material:           Aluminio 6061-T6")
print(f"Modulo E:           {E:,} MPa")
print(f"Tensao escoamento:  {sigma_yield} MPa")
print(f"Poisson (nu):       {nu}")
print(f"Dimensoes:          {W} x {H} x {t} mm")
print(f"Peso da chapa:      {plate_mass:.2f} kg ({plate_weight:.1f} N)")
print(f"Rigidez flexural D: {D:,.0f} N·mm")

print(f"\n--- GEOMETRIA DOS APOIOS ---")
for name, (x, y) in supports.items():
    print(f"  {name}: ({x:.1f}, {y:.1f}) mm")
print(f"  Vao X (entre apoios): {span_x:.1f} mm")
print(f"  Vao Y (entre apoios): {span_y:.1f} mm")
print(f"  Balanco lateral:      {overhang_left:.1f} mm")
print(f"  Balanco vert.:        {overhang_bottom:.1f} mm")

# =============================================================================
# MODELO 1: VIGA SIMPLESMENTE APOIADA (conservador)
# Pior caso: carga no centro do maior vao
# =============================================================================

print(f"\n{'=' * 72}")
print("MODELO 1: VIGA (conservador — ignora rigidez 2D)")
print("Viga simplesmente apoiada, carga pontual no centro do vao.")
print(f"Vao usado: {span_x:.1f} mm (maior vao)")
print(f"Largura efetiva: {H:.0f} mm (largura total da chapa)")
print("=" * 72)

I_beam = H * t**3 / 12  # mm⁴ (viga com largura = H)
L = span_x

print(f"\nI (viga, b={H}mm):  {I_beam:,.0f} mm^4")
print(f"{'─' * 72}")
print(f"{'Cenario':<45} {'P (N)':>8} {'delta':>8} {'sigma':>8} {'FS':>6}")
print(f"{'─' * 72}")

for name, mass_kg, multiplier in scenarios:
    P = mass_kg * g * multiplier

    # Deflexao: delta = P * L³ / (48 * E * I)
    delta = P * L**3 / (48 * E * I_beam)

    # Tensao maxima no centro: sigma = P * L / (4 * W_section)
    # W_section = I / (t/2) = modulo de secao
    W_section = I_beam / (t / 2)
    sigma_max = P * L / (4 * W_section)

    # Fator de seguranca
    fs = sigma_yield / sigma_max if sigma_max > 0 else float('inf')

    status = "OK" if fs >= 2.0 else ("ATENCAO" if fs >= 1.5 else "CRITICO")

    print(f"  {name:<43} {P:>8.0f} {delta:>7.2f}mm {sigma_max:>7.1f}MPa {fs:>5.1f} {status}")

# =============================================================================
# MODELO 2: PLACA DE KIRCHHOFF (mais realista)
# Placa retangular sobre 4 apoios pontuais
# Solucao por serie de Navier (dupla serie de Fourier)
# =============================================================================

print(f"\n{'=' * 72}")
print("MODELO 2: PLACA DE KIRCHHOFF (realista — rigidez 2D)")
print("Placa retangular sobre 4 apoios pontuais, carga no centro.")
print("Solucao por serie dupla de Fourier (Navier).")
print("=" * 72)

def plate_deflection_4_supports(P, a, b, t, E, nu,
                                  sup_coords, load_x, load_y,
                                  eval_x, eval_y, n_terms=50):
    """
    Calcula deflexao de placa retangular sobre 4 apoios pontuais.

    Usa principio de superposicao:
    - Placa simplesmente apoiada nas bordas com carga P no centro
    - Correcao para apoios pontuais (reacoes nos 4 pontos)

    Aproximacao: trata como placa simplesmente apoiada nas bordas
    (subestima deflexao, pois apoios pontuais dao menos rigidez).
    Depois aplica fator de correcao de 1.5-2.0x.

    Para resultado mais preciso, usar FEA.
    """
    D_val = E * t**3 / (12 * (1 - nu**2))

    w = 0.0
    for m in range(1, n_terms + 1, 2):  # impares
        for n in range(1, n_terms + 1, 2):
            alpha_mn = (m * np.pi / a)**2 + (n * np.pi / b)**2

            # Carga no ponto (load_x, load_y)
            Qmn = (4 * P / (a * b)) * np.sin(m * np.pi * load_x / a) * \
                   np.sin(n * np.pi * load_y / b)

            # Deflexao no ponto (eval_x, eval_y)
            w += (Qmn / (D_val * alpha_mn**2)) * \
                 np.sin(m * np.pi * eval_x / a) * \
                 np.sin(n * np.pi * eval_y / b)

    return w


def plate_stress_max(P, a, b, t, E, nu, n_terms=50):
    """
    Tensao maxima de flexao no centro de placa simplesmente apoiada
    com carga concentrada no centro.
    """
    D_val = E * t**3 / (12 * (1 - nu**2))

    Mx = 0.0  # Momento fletor em x
    My = 0.0  # Momento fletor em y

    cx, cy = a / 2, b / 2  # centro

    for m in range(1, n_terms + 1, 2):
        for n in range(1, n_terms + 1, 2):
            alpha_mn = (m * np.pi / a)**2 + (n * np.pi / b)**2

            Qmn = (4 * P / (a * b)) * np.sin(m * np.pi * 0.5) * \
                   np.sin(n * np.pi * 0.5)  # carga no centro

            wmn = Qmn / (D_val * alpha_mn**2)

            sin_mx = np.sin(m * np.pi * cx / a)
            sin_ny = np.sin(n * np.pi * cy / b)

            d2w_dx2 = -wmn * (m * np.pi / a)**2 * sin_mx * sin_ny
            d2w_dy2 = -wmn * (n * np.pi / b)**2 * sin_mx * sin_ny

            Mx += -D_val * (d2w_dx2 + nu * d2w_dy2)
            My += -D_val * (d2w_dy2 + nu * d2w_dx2)

    # Tensao = M * (t/2) / I = M / W_section = 6*M / t²
    sigma_x = 6 * abs(Mx) / t**2
    sigma_y = 6 * abs(My) / t**2

    return max(sigma_x, sigma_y)


# Usar vao entre apoios como dimensoes efetivas da placa
a_eff = span_x  # 475 mm
b_eff = span_y  # 334 mm

# Fator de correcao para apoios pontuais vs bordas apoiadas
# Apoios pontuais dao ~1.5-2x mais deflexao que bordas apoiadas completas
POINT_SUPPORT_FACTOR = 1.8  # conservador

print(f"\nVao efetivo: {a_eff:.0f} x {b_eff:.0f} mm")
print(f"Fator correcao apoios pontuais: {POINT_SUPPORT_FACTOR}x")
print(f"D (rigidez flexural): {D:,.0f} N·mm")

print(f"\n{'─' * 72}")
print(f"{'Cenario':<45} {'P (N)':>8} {'delta':>8} {'sigma':>8} {'FS':>6}")
print(f"{'─' * 72}")

for name, mass_kg, multiplier in scenarios:
    P = mass_kg * g * multiplier

    # Deflexao no centro (placa simply supported, carga no centro)
    delta_ss = plate_deflection_4_supports(
        P, a_eff, b_eff, t, E, nu,
        sup_coords=None,
        load_x=a_eff / 2, load_y=b_eff / 2,
        eval_x=a_eff / 2, eval_y=b_eff / 2,
        n_terms=80
    )

    # Correcao para apoios pontuais
    delta = abs(delta_ss) * POINT_SUPPORT_FACTOR

    # Tensao maxima
    sigma = plate_stress_max(P, a_eff, b_eff, t, E, nu, n_terms=80)
    sigma *= POINT_SUPPORT_FACTOR  # correcao conservadora

    fs = sigma_yield / sigma if sigma > 0 else float('inf')

    status = "OK" if fs >= 2.0 else ("ATENCAO" if fs >= 1.5 else "CRITICO")

    print(f"  {name:<43} {P:>8.0f} {delta:>7.2f}mm {sigma:>7.1f}MPa {fs:>5.1f} {status}")

# =============================================================================
# ANALISE DE ESPESSURAS ALTERNATIVAS
# =============================================================================

print(f"\n{'=' * 72}")
print("COMPARATIVO DE ESPESSURAS — Deflexao no centro (atleta 120 kg, DJ 5x BW)")
print("=" * 72)

P_ref = 120 * g * 5  # 5884 N (DJ pico)

thicknesses = [4, 5, 6, 8, 10, 12, 15]

print(f"\n{'Espessura':>10} {'Peso chapa':>12} {'delta (viga)':>14} {'delta (placa)':>14} {'sigma':>10} {'FS':>6}")
print(f"{'─' * 72}")

for tk in thicknesses:
    # Peso
    mass_k = (W * H * tk * 1e-9) * rho_al

    # Viga
    I_k = H * tk**3 / 12
    delta_beam = P_ref * L**3 / (48 * E * I_k)

    # Placa (Kirchhoff + correcao)
    delta_plate = abs(plate_deflection_4_supports(
        P_ref, a_eff, b_eff, tk, E, nu,
        None, a_eff/2, b_eff/2, a_eff/2, b_eff/2, 80
    )) * POINT_SUPPORT_FACTOR

    sigma_k = plate_stress_max(P_ref, a_eff, b_eff, tk, E, nu, 80) * POINT_SUPPORT_FACTOR
    fs_k = sigma_yield / sigma_k if sigma_k > 0 else float('inf')

    marker = " <<<" if tk == t else ""
    print(f"  {tk:>6} mm   {mass_k:>8.2f} kg   {delta_beam:>10.2f} mm   {delta_plate:>10.2f} mm   {sigma_k:>7.1f}MPa {fs_k:>5.1f}{marker}")

# =============================================================================
# CRITERIOS DE ACEITACAO
# =============================================================================

print(f"\n{'=' * 72}")
print("CRITERIOS DE ACEITACAO")
print("=" * 72)

print("""
Para plataformas de forca, os criterios tipicos sao:

  1. DEFLEXAO MAXIMA: < 0.5 mm no centro sob carga de operacao
     - Deflexao excessiva altera a distribuicao de carga entre celulas
     - Afeta a precisao da medicao (offset entre celulas)
     - Criterio conservador para pesquisa: < 0.2 mm

  2. TENSAO: Fator de seguranca (FS) >= 3.0 para carga de operacao
     - Aluminio 6061-T6: sigma_yield = 276 MPa
     - Para cargas de impacto (DJ): FS >= 2.0 minimo

  3. FREQUENCIA NATURAL: > 500 Hz (muito acima da taxa de amostragem)
     - Se a frequencia natural da placa for proxima de 1000 Hz,
       pode haver ressonancia com o sinal de forca
""")

# Frequencia natural aproximada (placa retangular simplesmente apoiada)
# f = (pi/2) * sqrt(D / (rho * t)) * ((m/a)² + (n/b)²)
rho_plate = rho_al * 1e-9  # kg/mm³
f_nat = (np.pi / 2) * np.sqrt(D / (rho_plate * t)) * \
        np.sqrt((1/a_eff)**2 + (1/b_eff)**2) * (1000 / (2 * np.pi))

# Simplificado: modo fundamental
f1 = (np.pi / (2 * a_eff**2)) * np.sqrt(D / (rho_plate * t)) * \
     (1 + (a_eff / b_eff)**2)

print(f"  Frequencia natural estimada (modo 1): ~{f1:.0f} Hz")
if f1 > 500:
    print(f"  Status: OK (bem acima de 500 Hz)")
else:
    print(f"  Status: ATENCAO (proxima da taxa de amostragem)")

# =============================================================================
# RECOMENDACAO
# =============================================================================

print(f"\n{'=' * 72}")
print("RECOMENDACAO")
print("=" * 72)

# Calcular deflexao no cenario critico (120kg, DJ 5x) para espessura atual
P_crit = 120 * g * 5
delta_atual = abs(plate_deflection_4_supports(
    P_crit, a_eff, b_eff, t, E, nu,
    None, a_eff/2, b_eff/2, a_eff/2, b_eff/2, 80
)) * POINT_SUPPORT_FACTOR

sigma_atual = plate_stress_max(P_crit, a_eff, b_eff, t, E, nu, 80) * POINT_SUPPORT_FACTOR
fs_atual = sigma_yield / sigma_atual

# Encontrar espessura minima para delta < 0.5mm no DJ 5x
for tk_min in range(6, 25):
    d_test = abs(plate_deflection_4_supports(
        P_crit, a_eff, b_eff, tk_min, E, nu,
        None, a_eff/2, b_eff/2, a_eff/2, b_eff/2, 80
    )) * POINT_SUPPORT_FACTOR
    if d_test < 0.5:
        break

mass_min = (W * H * tk_min * 1e-9) * rho_al
mass_atual = (W * H * t * 1e-9) * rho_al

print(f"""
  Espessura atual: {t} mm
  Deflexao no cenario critico (120kg DJ 5x): {delta_atual:.2f} mm
  Tensao maxima: {sigma_atual:.1f} MPa (FS = {fs_atual:.1f})

  Para deflexao < 0.5 mm no DJ 5x BW:
    Espessura minima recomendada: {tk_min} mm
    Peso da chapa: {mass_min:.2f} kg (atual: {mass_atual:.2f} kg)
    Aumento: +{mass_min - mass_atual:.2f} kg

  NOTA: Esta analise usa modelo analitico com fator de correcao
  para apoios pontuais (1.8x). Para validacao definitiva,
  recomenda-se simulacao FEA (elementos finitos) ou teste fisico.
  O modelo e conservador — a deflexao real tende a ser menor.
""")
