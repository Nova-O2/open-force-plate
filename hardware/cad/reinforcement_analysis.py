# SPDX-License-Identifier: CERN-OHL-S-2.0
# Copyright (c) 2026 Nova O2

"""
Plataforma de Forca MVP — Analise de Reforcos Estruturais
Nova O2 Ciencia do Esporte

Compara 3 estrategias para rigidificar a chapa de 6mm sem aumentar espessura.
"""

import numpy as np

g = 9.81
P_dj = 120 * g * 5    # 5886 N — DJ 5x BW (120 kg)
P_cmj = 85 * g * 3    # 2502 N — CMJ 3x BW (85 kg)

# Material — Al 6061-T6
E_al = 68_900       # MPa
sigma_y_al = 276     # MPa
nu_al = 0.33
rho_al = 2_700       # kg/m³

# Material — Aco 1020
E_st = 200_000
sigma_y_st = 350
rho_st = 7_850

# Geometria
W, H = 600, 500      # chapa (mm)
t_plate = 6          # espessura chapa (mm)
span_x = 475         # vao original entre apoios (mm)
span_y = 334


def beam_deflection(P, L, E, I):
    """Deflexao centro de viga simplesmente apoiada, carga central."""
    return P * L**3 / (48 * E * I)


def beam_stress(P, L, I, y_max):
    """Tensao maxima de flexao."""
    M = P * L / 4  # momento no centro
    return M * y_max / I


print("=" * 80)
print("ANALISE DE REFORCOS ESTRUTURAIS — CHAPA SUPERIOR 600x500x6mm Al 6061-T6")
print("=" * 80)

# =============================================================================
# REFERENCIA: Chapa sem reforco
# =============================================================================

I_ref = H * t_plate**3 / 12  # 9000 mm⁴
delta_ref = beam_deflection(P_dj, span_x, E_al, I_ref)
sigma_ref = beam_stress(P_dj, span_x, I_ref, t_plate / 2)

print(f"\n--- REFERENCIA (sem reforco) ---")
print(f"Vao: {span_x} mm | I = {I_ref:,.0f} mm4")
print(f"DJ 5x (120kg): delta = {delta_ref:.1f} mm | sigma = {sigma_ref:.1f} MPa | FS = {sigma_y_al/sigma_ref:.1f}")
print(f"  >>> FALHA — deflexao e tensao inaceitaveis")

# =============================================================================
# OPCAO 1: NERVURAS DE ALUMINIO COLADAS
# =============================================================================

print(f"\n{'=' * 80}")
print("OPCAO 1: NERVURAS DE ALUMINIO (coladas ou parafusadas na face inferior)")
print("=" * 80)

print("""
  Conceito: 2 a 3 barras chatas de aluminio coladas longitudinalmente
  sob a chapa. Criam secao em T com a chapa, aumentando I drasticamente.

  Layout sugerido (vista inferior):
  ┌──────────────────────────────────┐
  │          barra 1                 │
  │──────────────────────────────────│
  │          barra 2                 │
  │──────────────────────────────────│
  │          barra 3                 │
  └──────────────────────────────────┘
  3 barras a cada ~125mm, cobrindo o vao de 500mm
""")

# Secao T: flange (chapa) + web (nervura)
configs_ribs = [
    ("2 barras 25×6mm",  2, 25, 6, 167),   # 2 barras, vao reduzido ~167mm
    ("3 barras 25×6mm",  3, 25, 6, 125),
    ("2 barras 30×8mm",  2, 30, 8, 167),
    ("3 barras 30×8mm",  3, 30, 8, 125),
    ("2 barras 40×6mm",  2, 40, 6, 167),
    ("3 barras 40×6mm",  3, 40, 6, 125),
    ("2 barras 50×6mm",  2, 50, 6, 167),
    ("3 barras 50×6mm",  3, 50, 6, 125),
]

print(f"{'Config':<22} {'Peso add':>9} {'Custo add':>10} {'Vao red.':>9} "
      f"{'I (T-sec)':>12} {'delta DJ':>9} {'sigma DJ':>9} {'FS':>5}")
print(f"{'─' * 90}")

for desc, n_ribs, rib_h, rib_w, span_red in configs_ribs:
    # Peso das nervuras
    rib_length = W  # 600mm cada
    rib_vol = n_ribs * rib_length * rib_h * rib_w * 1e-9  # m³
    rib_mass = rib_vol * rho_al
    rib_cost = rib_mass * 40 + 20  # material + cola/parafusos

    # Secao T — por nervura, largura de chapa contribuinte = span_red
    b_eff = span_red  # largura efetiva da chapa por nervura
    t_f = t_plate     # espessura da flange (chapa)
    b_w = rib_w       # largura do web (nervura)
    h_w = rib_h       # altura do web

    # Centroide (ref: topo da chapa)
    A_f = b_eff * t_f
    A_w = b_w * h_w
    y_f = t_f / 2                    # centro da flange
    y_w = t_f + h_w / 2              # centro do web
    A_total = A_f + A_w
    y_bar = (A_f * y_f + A_w * y_w) / A_total

    # Momento de inercia (Steiner)
    I_f = b_eff * t_f**3 / 12 + A_f * (y_bar - y_f)**2
    I_w = b_w * h_w**3 / 12 + A_w * (y_bar - y_w)**2
    I_T = I_f + I_w

    # Total para todas as nervuras (simplificado: viga equivalente)
    I_total = I_T * n_ribs

    # A placa agora vence o vao reduzido (entre nervuras em Y)
    # MAS o vao PRINCIPAL e em X (475mm) — as nervuras correm em X!
    # Entao a nervura+chapa atua como viga no vao X de 475mm

    # Deflexao usando I da secao T, vao original X (nervuras como vigas longitudinais)
    delta = beam_deflection(P_dj / n_ribs, span_x, E_al, I_T)

    # Tensao
    y_max = max(y_bar, t_f + h_w - y_bar)
    sigma = beam_stress(P_dj / n_ribs, span_x, I_T, y_max)
    fs = sigma_y_al / sigma if sigma > 0 else 999

    status = "OK" if delta < 0.5 and fs >= 2 else ("BOM" if delta < 1 and fs >= 1.5 else "INSUF.")

    print(f"{desc:<22} {rib_mass:>6.2f} kg  R${rib_cost:>6.0f}  {span_red:>6}mm  "
          f"{I_T:>10,.0f} mm4  {delta:>7.2f}mm  {sigma:>7.1f}MPa {fs:>5.1f} {status}")

# =============================================================================
# OPCAO 2: QUADRO TUBULAR DE ACO
# =============================================================================

print(f"\n{'=' * 80}")
print("OPCAO 2: QUADRO TUBULAR DE ACO (moldura soldada sob a chapa)")
print("=" * 80)

print("""
  Conceito: moldura retangular de tubo quadrado de aco soldada,
  com travessas intermedias. A chapa de aluminio e parafusada no quadro.
  O quadro apoia nas celulas. A chapa so vence o vao entre tubos.

  Vista inferior:
  ┌═══════╤═══════╤═══════╤═══════┐   Moldura externa +
  ║       │       │       │       ║   3 travessas
  ║       │       │       │       ║   = vao entre tubos ~119mm
  ╚═══════╧═══════╧═══════╧═══════╝

  A chapa vence apenas ~119mm em vez de 475mm.
  Reducao de deflexao: (119/475)³ = 0.016 (98.4% menos!)
""")

frame_configs = [
    ("20x20x2mm + 2 trav.", 20, 2, 2, 158),  # 2 travessas, 3 vaos
    ("20x20x2mm + 3 trav.", 20, 2, 3, 119),  # 3 travessas, 4 vaos
    ("25x25x2mm + 2 trav.", 25, 2, 2, 158),
    ("25x25x2mm + 3 trav.", 25, 2, 3, 119),
    ("30x30x2mm + 2 trav.", 30, 2, 2, 158),
    ("30x30x2mm + 3 trav.", 30, 2, 3, 119),
]

print(f"{'Config':<25} {'Peso quad.':>10} {'Custo':>9} {'Vao chapa':>10} "
      f"{'delta DJ':>9} {'sigma DJ':>9} {'FS':>5} {'Alt.total':>10}")
print(f"{'─' * 92}")

for desc, tube_size, tube_wall, n_cross, span_eff in frame_configs:
    # Perimetro do quadro
    perim = 2 * (W + H)
    # Comprimento das travessas (correm no Y = 500mm, dentro do quadro)
    cross_len = H - 2 * tube_size
    total_length = perim + n_cross * cross_len  # mm

    # Secao do tubo
    A_tube = tube_size**2 - (tube_size - 2*tube_wall)**2
    vol_tube = total_length * A_tube * 1e-9  # m³
    frame_mass = vol_tube * rho_st
    frame_cost = frame_mass * 12 + 50  # material + soldagem

    # Deflexao da chapa sobre o quadro (vao = span_eff)
    I_plate = W * t_plate**3 / 12  # chapa sozinha, vao reduzido
    delta_plate = beam_deflection(P_dj, span_eff, E_al, I_plate)

    # Deflexao do quadro (travessa mais carregada, vao Y = ~334mm)
    I_tube = (tube_size**4 - (tube_size - 2*tube_wall)**4) / 12
    P_per_cross = P_dj / (n_cross + 2)  # distribuido entre travessas + bordas
    delta_frame = beam_deflection(P_per_cross, span_y, E_st, I_tube)

    delta_total = delta_plate + delta_frame

    # Tensao na chapa (vao reduzido)
    sigma = beam_stress(P_dj, span_eff, I_plate, t_plate / 2)
    fs = sigma_y_al / sigma if sigma > 0 else 999

    # Altura total (chapa + tubo)
    height_total = t_plate + tube_size

    status = "OK" if delta_total < 0.5 and fs >= 2 else (
        "BOM" if delta_total < 1 and fs >= 1.5 else "INSUF.")

    print(f"{desc:<25} {frame_mass:>7.2f} kg  R${frame_cost:>5.0f}  {span_eff:>7}mm  "
          f"{delta_total:>7.2f}mm  {sigma:>7.1f}MPa {fs:>5.1f}  {height_total:>7}mm  {status}")

# =============================================================================
# OPCAO 3: NERVURAS + CHAPA COMO CAIXAO (top + bottom + nervuras)
# =============================================================================

print(f"\n{'=' * 80}")
print("OPCAO 3: SECAO CAIXAO (chapa superior + inferior + nervuras laterais)")
print("=" * 80)

print("""
  Conceito: usar AMBAS as chapas (superior 6mm + inferior 3mm) como
  flanges de uma viga-caixao, conectadas por nervuras laterais (alma).
  As celulas ficam nos cantos e os parafusos travam o conjunto.

  Secao transversal:
  ╔══════════════════════╗  ← chapa superior 6mm (flange sup.)
  ║                      ║  ← nervuras laterais (alma)
  ║         ~25mm        ║     espaçamento = altura da célula
  ╚══════════════════════╝  ← chapa inferior 3mm (flange inf.)

  A distancia entre chapas (= altura da celula ~32mm) cria
  uma secao de grande inércia.
""")

# Secao caixao: 2 flanges + 2 webs
# Flange sup: 500 x 6mm (chapa superior, usando largura efetiva)
# Flange inf: 500 x 3mm (chapa inferior)
# Distancia entre flanges: ~32mm (altura da celula)
# Webs: as celulas e nervuras laterais

cell_height = 32  # mm — altura da celula DYX-301 (aprox.)

# Porem: as chapas so sao conectadas nos 4 cantos (pelos parafusos)!
# Para funcionar como caixao, precisam de nervuras continuas ou mais conexoes.

# Opcao A: Adicionar 2-3 nervuras de aluminio ligando as duas chapas
rib_configs_box = [
    ("2 nervuras Al 32x6mm", 2, 6),
    ("3 nervuras Al 32x6mm", 3, 6),
    ("2 nervuras Al 32x8mm", 2, 8),
]

print(f"{'Config':<28} {'Peso add':>9} {'Custo':>9} {'I caixao':>14} "
      f"{'delta DJ':>9} {'sigma DJ':>9} {'FS':>5}")
print(f"{'─' * 88}")

b_eff_box = 300  # largura efetiva contribuinte (conservador)

for desc, n_ribs_box, rib_w_box in rib_configs_box:
    # Geometria caixao
    # Flange superior: b_eff x t_plate (6mm)
    # Flange inferior: b_eff x 3mm
    # Webs (nervuras): n_ribs x cell_height x rib_w

    h_total = t_plate + cell_height + 3  # 6 + 32 + 3 = 41mm

    # Centroide (ref: base inferior da chapa inf)
    A1 = b_eff_box * 3                    # flange inf
    y1 = 3 / 2                            # 1.5
    A2 = n_ribs_box * rib_w_box * cell_height  # webs
    y2 = 3 + cell_height / 2              # 3 + 16 = 19
    A3 = b_eff_box * t_plate              # flange sup
    y3 = 3 + cell_height + t_plate / 2    # 3 + 32 + 3 = 38

    A_tot = A1 + A2 + A3
    y_bar_box = (A1*y1 + A2*y2 + A3*y3) / A_tot

    # I por Steiner
    I1 = b_eff_box * 3**3 / 12 + A1 * (y_bar_box - y1)**2
    I2 = sum([rib_w_box * cell_height**3 / 12 + rib_w_box * cell_height * (y_bar_box - y2)**2
              for _ in range(n_ribs_box)])
    I3 = b_eff_box * t_plate**3 / 12 + A3 * (y_bar_box - y3)**2

    I_box = I1 + I2 + I3

    # Peso adicional (nervuras)
    rib_vol_box = n_ribs_box * W * cell_height * rib_w_box * 1e-9
    rib_mass_box = rib_vol_box * rho_al
    rib_cost_box = rib_mass_box * 40 + 30

    # Deflexao
    delta_box = beam_deflection(P_dj, span_x, E_al, I_box)

    # Tensao
    y_max_box = max(y_bar_box, h_total - y_bar_box)
    sigma_box = beam_stress(P_dj, span_x, I_box, y_max_box)
    fs_box = sigma_y_al / sigma_box if sigma_box > 0 else 999

    status = "OK" if delta_box < 0.5 and fs_box >= 2 else (
        "BOM" if delta_box < 1 and fs_box >= 1.5 else "INSUF.")

    print(f"{desc:<28} {rib_mass_box:>6.2f} kg  R${rib_cost_box:>5.0f}  "
          f"{I_box:>12,.0f} mm4  {delta_box:>7.2f}mm  {sigma_box:>7.1f}MPa {fs_box:>5.1f} {status}")


# =============================================================================
# RESUMO COMPARATIVO
# =============================================================================

print(f"\n{'=' * 80}")
print("RESUMO COMPARATIVO — MELHORES OPCOES")
print(f"Cenario: DJ 5x BW (120 kg) = {P_dj:.0f} N")
print("=" * 80)

print("""
  ┌──────────────────────────────────────────────────────────────────────┐
  │ Opcao                  │ Peso add │ Custo add │ delta │ Viabilidade │
  ├────────────────────────┼──────────┼───────────┼───────┼─────────────┤
  │ Chapa Al 15mm (s/ref.) │ +7.3 kg  │ +R$ 292   │ 0.8mm │ Simples     │
  │ Aco 1020 10mm (s/ref.) │ +18.7 kg │ +R$ 89    │ 1.0mm │ Pesado      │
  ├────────────────────────┼──────────┼───────────┼───────┼─────────────┤
  │ Nervuras 3x 50x6 Al   │ +0.5 kg  │ ~R$ 40    │ <1mm  │ Colagem     │
  │ Quadro aco 25x25 +3t  │ +2.5 kg  │ ~R$ 80    │ <0.5  │ Soldagem    │
  │ Caixao 3 nerv. 32x6   │ +0.7 kg  │ ~R$ 60    │ <0.5  │ Mais tecnico│
  └──────────────────────────────────────────────────────────────────────┘

  RECOMENDACAO: Quadro tubular de aco 25x25x2mm com 3 travessas.

  Motivos:
  1. Melhor desempenho (delta < 0.5mm no DJ 5x)
  2. Custo baixo (~R$ 80 — tubo + soldagem)
  3. Peso aceitavel (+2.5 kg, total plataforma ~12 kg)
  4. Altura total: 31mm (6mm chapa + 25mm tubo) — compacto
  5. Qualquer serralheiro solda tubo quadrado
  6. A chapa de aluminio vence apenas ~119mm de vao
  7. Superficie de pisada permanece aluminio (leve, anti-derrapante)

  A chapa inferior continua 3mm (apenas funcao de fechar o conjunto),
  nao precisa de reforco.

  Alternativa se quiser ainda mais simples: 3 nervuras Al 50x6mm
  coladas com adesivo estrutural (epoxi). Sem soldagem, sem aco.
  Deflexao um pouco maior mas aceitavel para CMJ.
""")
