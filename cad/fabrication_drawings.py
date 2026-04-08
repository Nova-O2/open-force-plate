"""
Plataforma de Forca MVP — Desenhos de Fabricacao
Nova O2 Ciencia do Esporte

Gera 5 PDFs de fabricacao:
1. fab_chapa_superior.pdf — Chapa superior 600x500mm, 6mm aluminio, cantos R30, furos escareados M10
2. fab_chapa_inferior.pdf — Chapa inferior 527x396mm, 3mm aluminio, cantos chanfrados 15x15
3. fab_pezinho.pdf — Pezinho torneado com colar (x4)
4. fab_junta.pdf — Junta de aco (x4)
5. fab_montagem.pdf — Vista explodida de montagem
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Polygon
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.path import Path
import matplotlib.image as mpimg
import numpy as np
from datetime import date

# =============================================================================
# CONSTANTES
# =============================================================================

ICON_PATH = '/workspace/03-engineering/nova-o2/force-plate/cad/nova_o2_icon.png'
OUT_DIR = '/workspace/03-engineering/nova-o2/force-plate/cad'
ORANGE = '#E8820C'
DARK = '#333333'
LIGHT_GRAY = '#F0F0F0'
MID_GRAY = '#999999'
TODAY = date.today().strftime('%d/%m/%Y')

# Chapa superior
TOP_W, TOP_H = 600, 500
TOP_THICK = 6.35
CORNER_R = 30

# Chapa inferior
BOT_W, BOT_H = 527, 396
BOT_THICK = 3
BOT_X0 = (TOP_W - BOT_W) / 2  # 36.5
BOT_Y0 = (TOP_H - BOT_H) / 2  # 52.0
BOT_CHAMFER = 15  # chanfro 45 graus nos cantos

# Furos — posicoes absolutas (ref: chapa superior, origem canto inf-esq)
HOLES_ABS = {
    'C1': [(56.7, 428.1), (68.3, 406.0)],
    'C2': [(543.3, 428.1), (531.7, 406.0)],
    'C3': [(56.7, 71.9), (68.3, 94.0)],
    'C4': [(543.3, 71.9), (531.7, 94.0)],
}
HOLE_DIA = 11  # M10
HOLE_SPACING = 25.0
COUNTERSINK_DIA = 20  # escareamento DIN 7991 M10

# Junta
GASKET_L, GASKET_W, GASKET_T = 56, 32, 2

# Pezinho (com colar)
ROD_DIA = 12
ROD_LENGTH = 32
COLLAR_DIA = 20
COLLAR_H = 5
CHAMFER_H = 6
BASE_DIA = 60
BASE_H = 8
RUBBER_H = 1
TOTAL_FOOT = ROD_LENGTH + COLLAR_H + CHAMFER_H + BASE_H + RUBBER_H  # 52mm


# =============================================================================
# BLOCO DE TITULO
# =============================================================================

def add_title_block(fig, piece_name, material, thickness, quantity, notes=""):
    ax = fig.add_axes([0.0, 0.0, 1.0, 0.11])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 11)
    ax.axis('off')

    bg = FancyBboxPatch((0, 0), 100, 11, boxstyle="square,pad=0",
                         fc='white', ec='none', zorder=1)
    ax.add_patch(bg)
    ax.plot([0, 100], [11, 11], color=ORANGE, lw=2.5, zorder=3)
    ax.plot([0, 100], [0, 0], color=ORANGE, lw=0.5, zorder=3)

    try:
        logo = mpimg.imread(ICON_PATH)
        im = OffsetImage(logo, zoom=0.03)
        ab = AnnotationBbox(im, (3, 5.5), frameon=False, zorder=3)
        ax.add_artist(ab)
    except:
        pass

    ax.text(7, 8.5, u'NOVA O2 CI\u00caNCIA DO ESPORTE', fontsize=9, fontweight='bold',
            color=ORANGE, va='center', zorder=2)
    ax.text(7, 5.5, u'DESENHO DE FABRICA\u00c7\u00c3O', fontsize=7,
            color=DARK, va='center', zorder=2)
    ax.text(7, 3, u'Projeto: Plataforma de For\u00e7a MVP', fontsize=6,
            color=MID_GRAY, va='center', zorder=2)

    ix = 45
    ax.text(ix, 9.5, u'Pe\u00e7a:', fontsize=6, color=MID_GRAY, va='center')
    ax.text(ix + 4.5, 9.5, piece_name, fontsize=8, fontweight='bold',
            color=ORANGE, va='center')
    ax.text(ix, 7, f'Material: {material}', fontsize=6.5, color=DARK, va='center')
    ax.text(ix, 4.5, f'Espessura: {thickness}', fontsize=6.5, color=DARK, va='center')
    ax.text(ix, 2, f'Quantidade: {quantity}', fontsize=6.5, fontweight='bold',
            color=DARK, va='center')

    ax.text(85, 9.5, f'Data: {TODAY}', fontsize=6, color=MID_GRAY, va='center')
    ax.text(85, 7, 'Cotas em mm', fontsize=6, color=MID_GRAY, va='center')
    ax.text(85, 4.5, 'Escala: indicada', fontsize=6, color=MID_GRAY, va='center')
    if notes:
        ax.text(85, 2, notes, fontsize=5, color=MID_GRAY, va='center')

    for vx in [44, 83]:
        ax.plot([vx, vx], [0.5, 10.5], color='#DDD', lw=0.5, zorder=2)


# =============================================================================
# FUNCOES DE COTAGEM
# =============================================================================

def dim_h(ax, x1, x2, y, offset, text, fs=7, color=DARK):
    yc = y + offset
    ax.annotate('', xy=(x1, yc), xytext=(x2, yc),
                arrowprops=dict(arrowstyle='<->', color=color, lw=0.7))
    ax.text((x1 + x2) / 2, yc + (2.5 if offset > 0 else -2.5), text,
            ha='center', va='bottom' if offset > 0 else 'top',
            fontsize=fs, color=color, fontweight='bold',
            bbox=dict(fc='white', ec='none', pad=0.5))
    ax.plot([x1, x1], [y, yc], color='#BBB', lw=0.3, ls='--')
    ax.plot([x2, x2], [y, yc], color='#BBB', lw=0.3, ls='--')


def dim_v(ax, y1, y2, x, offset, text, fs=7, color=DARK):
    xc = x + offset
    ax.annotate('', xy=(xc, y1), xytext=(xc, y2),
                arrowprops=dict(arrowstyle='<->', color=color, lw=0.7))
    ax.text(xc + (3 if offset > 0 else -3), (y1 + y2) / 2, text,
            ha='left' if offset > 0 else 'right', va='center',
            fontsize=fs, color=color, fontweight='bold', rotation=90,
            bbox=dict(fc='white', ec='none', pad=0.5))
    ax.plot([x, xc], [y1, y1], color='#BBB', lw=0.3, ls='--')
    ax.plot([x, xc], [y2, y2], color='#BBB', lw=0.3, ls='--')


def dim_between(ax, p1, p2, offset_dir, text, fs=7, color=ORANGE):
    mx, my = (p1[0]+p2[0])/2, (p1[1]+p2[1])/2
    ax.annotate('', xy=p1, xytext=p2,
                arrowprops=dict(arrowstyle='<->', color=color, lw=0.8))
    ox, oy = offset_dir
    ax.text(mx + ox, my + oy, text, ha='center', va='center',
            fontsize=fs, color=color, fontweight='bold',
            bbox=dict(fc='white', ec='none', pad=0.5))


def draw_hole(ax, x, y, dia=11):
    c = plt.Circle((x, y), dia / 2, fill=False, ec='black', lw=1, zorder=4)
    ax.add_patch(c)
    s = dia / 2 + 3
    ax.plot([x - s, x + s], [y, y], color='black', lw=0.3, zorder=4)
    ax.plot([x, x], [y - s, y + s], color='black', lw=0.3, zorder=4)


def draw_countersunk_hole(ax, x, y, dia=11, cs_dia=20):
    """Furo escareado — circulo interno + externo tracejado."""
    inner = plt.Circle((x, y), dia / 2, fill=False, ec='black', lw=1, zorder=4)
    ax.add_patch(inner)
    outer = plt.Circle((x, y), cs_dia / 2, fill=False, ec='black', lw=0.6,
                        ls='--', zorder=4)
    ax.add_patch(outer)
    s = cs_dia / 2 + 2
    ax.plot([x - s, x + s], [y, y], color='black', lw=0.3, zorder=4)
    ax.plot([x, x], [y - s, y + s], color='black', lw=0.3, zorder=4)


def clean_axes(ax):
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)


def draw_rounded_rect(ax, x, y, w, h, r, **kwargs):
    defaults = dict(lw=2, ec='black', fc=LIGHT_GRAY, zorder=1)
    defaults.update(kwargs)
    verts = [
        (x + r, y), (x, y), (x, y + r),
        (x, y + h - r), (x, y + h), (x + r, y + h),
        (x + w - r, y + h), (x + w, y + h), (x + w, y + h - r),
        (x + w, y + r), (x + w, y), (x + w - r, y),
        (x + r, y),
    ]
    codes = [
        Path.MOVETO, Path.CURVE3, Path.CURVE3,
        Path.LINETO, Path.CURVE3, Path.CURVE3,
        Path.LINETO, Path.CURVE3, Path.CURVE3,
        Path.LINETO, Path.CURVE3, Path.CURVE3,
        Path.CLOSEPOLY,
    ]
    patch = patches.PathPatch(Path(verts, codes), **defaults)
    ax.add_patch(patch)


def draw_chamfered_rect(ax, x, y, w, h, c, **kwargs):
    """Retangulo com cantos chanfrados a 45 graus."""
    defaults = dict(lw=2, ec='black', fc=LIGHT_GRAY, zorder=1)
    defaults.update(kwargs)
    verts = [
        (x + c, y), (x, y + c),                    # inf-esq
        (x, y + h - c), (x + c, y + h),            # sup-esq
        (x + w - c, y + h), (x + w, y + h - c),    # sup-dir
        (x + w, y + c), (x + w - c, y),             # inf-dir
        (x + c, y),                                  # fechar
    ]
    codes = [
        Path.MOVETO, Path.LINETO,
        Path.LINETO, Path.LINETO,
        Path.LINETO, Path.LINETO,
        Path.LINETO, Path.LINETO,
        Path.CLOSEPOLY,
    ]
    patch = patches.PathPatch(Path(verts, codes), **defaults)
    ax.add_patch(patch)


# =============================================================================
# 1. CHAPA SUPERIOR
# =============================================================================

def draw_chapa_superior():
    fig = plt.figure(figsize=(14, 10))

    # === VISTA SUPERIOR ===
    ax1 = fig.add_axes([0.05, 0.25, 0.55, 0.68])
    ax1.set_title('VISTA SUPERIOR', fontsize=10, fontweight='bold', pad=8, color=DARK)

    draw_rounded_rect(ax1, 0, 0, TOP_W, TOP_H, CORNER_R)

    # Linhas de centro
    ax1.plot([TOP_W/2, TOP_W/2], [-5, TOP_H+5], color='#CCC', lw=0.5, ls='-.')
    ax1.plot([-5, TOP_W+5], [TOP_H/2, TOP_H/2], color='#CCC', lw=0.5, ls='-.')

    # Furos escareados
    for cell in HOLES_ABS.values():
        for hx, hy in cell:
            draw_countersunk_hole(ax1, hx, hy, HOLE_DIA, COUNTERSINK_DIA)

    # --- COTAS ---
    # Dimensoes gerais
    dim_h(ax1, 0, TOP_W, 0, -35, f'{TOP_W}', fs=9)
    dim_v(ax1, 0, TOP_H, 0, -40, f'{TOP_H}', fs=9)

    # Cotas dos furos — canto inferior esquerdo (C3)
    h1x, h1y = HOLES_ABS['C3'][0]  # 56.7, 71.9
    h2x, h2y = HOLES_ABS['C3'][1]  # 68.3, 94.0

    # X: borda esquerda aos furos (horizontais, abaixo e acima)
    dim_h(ax1, 0, h1x, h1y, -18, f'{h1x:.1f}', fs=6.5)
    dim_h(ax1, 0, h2x, h2y, 12, f'{h2x:.1f}', fs=6.5)

    # Y: borda inferior aos furos (verticais, a direita dos furos, espaçadas)
    dim_v(ax1, 0, h1y, h2x, 15, f'{h1y:.1f}', fs=6.5)
    dim_v(ax1, 0, h2y, h2x, 30, f'{h2y:.1f}', fs=6.5)

    # R30 — canto superior direito
    ax1.annotate(f'R{CORNER_R}', xy=(TOP_W - CORNER_R * 0.3, TOP_H - CORNER_R * 0.3),
                 xytext=(TOP_W - CORNER_R - 40, TOP_H - 15),
                 fontsize=8, color=ORANGE, fontweight='bold',
                 arrowprops=dict(arrowstyle='->', color=ORANGE, lw=0.8))

    ax1.text(TOP_W/2, TOP_H + 12, u'SIM\u00c9TRICO EM AMBOS OS EIXOS',
             ha='center', fontsize=7, color=MID_GRAY, style='italic')

    ax1.set_xlim(-55, TOP_W + 60)
    ax1.set_ylim(-55, TOP_H + 25)
    ax1.set_aspect('equal')
    clean_axes(ax1)

    # === VISTA FRONTAL ===
    ax2 = fig.add_axes([0.65, 0.60, 0.30, 0.25])
    ax2.set_title('VISTA FRONTAL', fontsize=9, fontweight='bold', pad=5, color=DARK)

    profile = patches.Rectangle((0, 0), TOP_W, TOP_THICK, lw=2,
                                 ec='black', fc=LIGHT_GRAY)
    ax2.add_patch(profile)

    # Indicacao de escareamento (V na face superior)
    for cell in HOLES_ABS.values():
        for hx, hy in cell:
            # Furo passante
            ax2.plot([hx, hx], [0, TOP_THICK], color='#CCC', lw=0.3, ls=':')
            # Escareamento (V)
            cs_half = COUNTERSINK_DIA / 2
            ax2.plot([hx - cs_half, hx, hx + cs_half],
                     [TOP_THICK, TOP_THICK - 5.5, TOP_THICK],
                     color='black', lw=0.8)

    dim_v(ax2, 0, TOP_THICK, 0, -25, f'{TOP_THICK}', fs=8)
    dim_h(ax2, 0, TOP_W, 0, -8, f'{TOP_W}', fs=7)

    ax2.set_xlim(-35, TOP_W + 15)
    ax2.set_ylim(-15, TOP_THICK + 12)
    ax2.set_aspect('equal')
    clean_axes(ax2)

    # === DETALHE — PAR DE FUROS ===
    ax3 = fig.add_axes([0.65, 0.17, 0.30, 0.37])

    h1x, h1y = HOLES_ABS['C3'][0]
    h2x, h2y = HOLES_ABS['C3'][1]
    cx_d = (h1x + h2x) / 2
    cy_d = (h1y + h2y) / 2
    margin = 30

    bg = patches.Rectangle((cx_d - margin, cy_d - margin), margin * 2, margin * 2,
                             lw=1, ec='#CCC', fc=LIGHT_GRAY, zorder=1)
    ax3.add_patch(bg)

    for hx, hy in [(h1x, h1y), (h2x, h2y)]:
        draw_countersunk_hole(ax3, hx, hy, HOLE_DIA, COUNTERSINK_DIA)

    # Cota entre centros — ESQUERDA do par
    dim_between(ax3, (h1x, h1y), (h2x, h2y), (-14, -2), f'{HOLE_SPACING}', fs=8)

    # Diametros
    ax3.text(h1x, h1y - 15, f'\u00d8{HOLE_DIA} passante\nescareado \u00d8{COUNTERSINK_DIA}\n(DIN 7991 M10)',
             ha='center', fontsize=6.5, color=DARK, fontweight='bold')

    # Angulo — DIREITA do par
    angle = np.degrees(np.arctan2(h2y - h1y, h2x - h1x))
    ax3.plot([h1x, h1x + 25], [h1y, h1y], color=MID_GRAY, lw=0.5, ls=':')
    theta = np.linspace(0, np.radians(angle), 30)
    r_arc = 18
    ax3.plot(h1x + r_arc * np.cos(theta), h1y + r_arc * np.sin(theta),
             color=ORANGE, lw=1.5)
    ax3.text(h1x + r_arc + 3, h1y + 8, f'~{angle:.0f}\u00b0',
             fontsize=9, color=ORANGE, fontweight='bold')

    # Titulo centralizado com o desenho
    ax3.text(cx_d, cy_d + margin + 8,
             u'DETALHE \u2014 Par de furos escareados\n(t\u00edpico, \u00d74 cantos)',
             ha='center', fontsize=9, fontweight='bold', color=DARK)

    ax3.set_xlim(cx_d - margin - 15, cx_d + margin + 25)
    ax3.set_ylim(cy_d - margin - 8, cy_d + margin + 18)
    ax3.set_aspect('equal')
    clean_axes(ax3)

    add_title_block(fig, 'Chapa superior', u'Alum\u00ednio 5052-F',
                    f'{TOP_THICK}mm (1/4")', '1 unidade',
                    f'Cantos R{CORNER_R}, furos escareados M10')

    fig.savefig(f'{OUT_DIR}/fab_chapa_superior.pdf', bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print("  -> fab_chapa_superior.pdf")


# =============================================================================
# 2. CHAPA INFERIOR
# =============================================================================

def draw_chapa_inferior():
    fig = plt.figure(figsize=(14, 10))

    holes_rel = {}
    for cell, pts in HOLES_ABS.items():
        holes_rel[cell] = [(hx - BOT_X0, hy - BOT_Y0) for hx, hy in pts]

    # === VISTA SUPERIOR ===
    ax1 = fig.add_axes([0.05, 0.25, 0.55, 0.68])
    ax1.set_title('VISTA SUPERIOR', fontsize=10, fontweight='bold', pad=8, color=DARK)

    draw_chamfered_rect(ax1, 0, 0, BOT_W, BOT_H, BOT_CHAMFER)

    ax1.plot([BOT_W/2, BOT_W/2], [-5, BOT_H+5], color='#CCC', lw=0.5, ls='-.')
    ax1.plot([-5, BOT_W+5], [BOT_H/2, BOT_H/2], color='#CCC', lw=0.5, ls='-.')

    for cell in holes_rel.values():
        for hx, hy in cell:
            draw_hole(ax1, hx, hy, HOLE_DIA)

    # Dimensoes gerais
    dim_h(ax1, 0, BOT_W, 0, -35, f'{BOT_W}', fs=9)
    dim_v(ax1, 0, BOT_H, 0, -40, f'{BOT_H}', fs=9)

    # Cotas dos furos — canto inferior esquerdo (C3)
    h1x, h1y = holes_rel['C3'][0]
    h2x, h2y = holes_rel['C3'][1]

    # X: borda esquerda aos furos (horizontais, abaixo e acima)
    dim_h(ax1, 0, h1x, h1y, -18, f'{h1x:.1f}', fs=6.5)
    dim_h(ax1, 0, h2x, h2y, 12, f'{h2x:.1f}', fs=6.5)

    # Y: borda inferior aos furos (verticais, a direita dos furos, espaçadas)
    dim_v(ax1, 0, h1y, h2x, 15, f'{h1y:.1f}', fs=6.5)
    dim_v(ax1, 0, h2y, h2x, 30, f'{h2y:.1f}', fs=6.5)

    # Chanfro — canto superior direito
    ch_x = BOT_W - BOT_CHAMFER
    ch_y = BOT_H - BOT_CHAMFER
    dim_h(ax1, ch_x, BOT_W, BOT_H, 12, f'{BOT_CHAMFER}', fs=7, color=ORANGE)
    dim_v(ax1, ch_y, BOT_H, BOT_W, 15, f'{BOT_CHAMFER}', fs=7, color=ORANGE)
    ax1.text(BOT_W - BOT_CHAMFER / 2 - 15, BOT_H - BOT_CHAMFER / 2 + 5,
             u'chanfro 45\u00b0', fontsize=6.5, color=ORANGE, fontweight='bold')

    ax1.text(BOT_W / 2, BOT_H + 12, u'SIM\u00c9TRICO EM AMBOS OS EIXOS',
             ha='center', fontsize=7, color=MID_GRAY, style='italic')

    ax1.set_xlim(-55, BOT_W + 60)
    ax1.set_ylim(-55, BOT_H + 25)
    ax1.set_aspect('equal')
    clean_axes(ax1)

    # === VISTA FRONTAL ===
    ax2 = fig.add_axes([0.65, 0.60, 0.30, 0.25])
    ax2.set_title('VISTA FRONTAL', fontsize=9, fontweight='bold', pad=5, color=DARK)

    profile = patches.Rectangle((0, 0), BOT_W, BOT_THICK, lw=2,
                                 ec='black', fc=LIGHT_GRAY)
    ax2.add_patch(profile)

    dim_v(ax2, 0, BOT_THICK, 0, -25, f'{BOT_THICK}', fs=8)
    dim_h(ax2, 0, BOT_W, 0, -8, f'{BOT_W}', fs=7)

    for cell in holes_rel.values():
        for hx, hy in cell:
            ax2.plot([hx - 3, hx + 3], [BOT_THICK, BOT_THICK], color='black', lw=1.5)
            ax2.plot([hx, hx], [0, BOT_THICK], color='#CCC', lw=0.3, ls=':')

    ax2.set_xlim(-35, BOT_W + 15)
    ax2.set_ylim(-15, BOT_THICK + 12)
    ax2.set_aspect('equal')
    clean_axes(ax2)

    # === DETALHE — PAR DE FUROS ===
    ax3 = fig.add_axes([0.65, 0.17, 0.30, 0.37])

    h1x, h1y = holes_rel['C3'][0]
    h2x, h2y = holes_rel['C3'][1]
    cx_d = (h1x + h2x) / 2
    cy_d = (h1y + h2y) / 2
    margin = 30

    bg = patches.Rectangle((cx_d - margin, cy_d - margin), margin * 2, margin * 2,
                             lw=1, ec='#CCC', fc=LIGHT_GRAY, zorder=1)
    ax3.add_patch(bg)

    for hx, hy in [(h1x, h1y), (h2x, h2y)]:
        draw_hole(ax3, hx, hy, HOLE_DIA)

    # Cota entre centros — ESQUERDA do par
    dim_between(ax3, (h1x, h1y), (h2x, h2y), (-14, -2), f'{HOLE_SPACING}', fs=8)

    ax3.text(h1x, h1y - 15, f'\u00d8{HOLE_DIA} passante',
             ha='center', fontsize=7, color=DARK, fontweight='bold')

    # Angulo — DIREITA do par
    angle = np.degrees(np.arctan2(h2y - h1y, h2x - h1x))
    ax3.plot([h1x, h1x + 25], [h1y, h1y], color=MID_GRAY, lw=0.5, ls=':')
    theta = np.linspace(0, np.radians(angle), 30)
    r_arc = 18
    ax3.plot(h1x + r_arc * np.cos(theta), h1y + r_arc * np.sin(theta),
             color=ORANGE, lw=1.5)
    ax3.text(h1x + r_arc + 3, h1y + 8, f'~{angle:.0f}\u00b0',
             fontsize=9, color=ORANGE, fontweight='bold')

    # Titulo centralizado com o desenho
    ax3.text(cx_d, cy_d + margin + 8,
             u'DETALHE \u2014 Par de furos\n(t\u00edpico, \u00d74 cantos)',
             ha='center', fontsize=9, fontweight='bold', color=DARK)

    ax3.set_xlim(cx_d - margin - 15, cx_d + margin + 25)
    ax3.set_ylim(cy_d - margin - 8, cy_d + margin + 18)
    ax3.set_aspect('equal')
    clean_axes(ax3)

    add_title_block(fig, 'Chapa inferior', u'Alum\u00ednio 5052-F',
                    f'{BOT_THICK}mm', '1 unidade',
                    f'Cantos chanfrados {BOT_CHAMFER}\u00d7{BOT_CHAMFER} a 45\u00b0')

    fig.savefig(f'{OUT_DIR}/fab_chapa_inferior.pdf', bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print("  -> fab_chapa_inferior.pdf")


# =============================================================================
# 3. PEZINHO TORNEADO (com colar)
# =============================================================================

def draw_pezinho():
    fig = plt.figure(figsize=(14, 10))

    ROD_R = ROD_DIA / 2
    COLLAR_R = COLLAR_DIA / 2
    BASE_R = BASE_DIA / 2

    cx = 80
    y_top = 110
    rod_bottom = y_top - ROD_LENGTH           # 78
    collar_bottom = rod_bottom - COLLAR_H     # 73
    chamfer_bottom = collar_bottom - CHAMFER_H # 67
    base_bottom = chamfer_bottom - BASE_H     # 59
    rub_bottom = base_bottom - RUBBER_H       # 58

    pc = '#D0D0D0'
    pe_c = '#444'

    # === VISTA EM CORTE ===
    ax1 = fig.add_axes([0.05, 0.25, 0.45, 0.68])
    ax1.set_title(u'VISTA EM CORTE (se\u00e7\u00e3o longitudinal)', fontsize=10,
                  fontweight='bold', pad=8, color=DARK)

    # Rosca
    rod = patches.Rectangle((cx - ROD_R, rod_bottom), ROD_DIA, ROD_LENGTH,
                              lw=1, ec=pe_c, fc=pc, zorder=2)
    ax1.add_patch(rod)
    for ty in np.arange(y_top - 1, rod_bottom + 1, -2):
        ax1.plot([cx - ROD_R - 1.5, cx + ROD_R + 1.5], [ty, ty - 1], color='#999', lw=0.3)

    # Colar
    collar = patches.Rectangle((cx - COLLAR_R, collar_bottom), COLLAR_DIA, COLLAR_H,
                                 lw=1, ec=pe_c, fc='#C0C0C0', zorder=2)
    ax1.add_patch(collar)

    # Chanfro
    chamfer = Polygon([
        (cx - COLLAR_R, collar_bottom), (cx + COLLAR_R, collar_bottom),
        (cx + BASE_R, chamfer_bottom), (cx - BASE_R, chamfer_bottom),
    ], closed=True, lw=1, ec=pe_c, fc=pc, zorder=2)
    ax1.add_patch(chamfer)

    # Base
    base = patches.Rectangle((cx - BASE_R, base_bottom), BASE_DIA, BASE_H,
                               lw=1, ec=pe_c, fc=pc, zorder=2)
    ax1.add_patch(base)

    # Borracha
    rub = patches.Rectangle((cx - BASE_R, rub_bottom), BASE_DIA, RUBBER_H * 2,
                              lw=0.8, ec='#222', fc='#444', zorder=2)
    ax1.add_patch(rub)

    # Linha de centro
    ax1.plot([cx, cx], [y_top + 5, rub_bottom - 5], color='#999', lw=0.5, ls='-.')

    # === COTAS ===

    # Diametros (horizontais) — sem sobreposicao
    dim_h(ax1, cx - ROD_R, cx + ROD_R, y_top - 3, 10, f'\u00d8{ROD_DIA}', fs=8)
    dim_h(ax1, cx - COLLAR_R, cx + COLLAR_R, rod_bottom, 5,
          f'\u00d8{COLLAR_DIA}', fs=8, color=ORANGE)
    dim_h(ax1, cx - BASE_R, cx + BASE_R, rub_bottom, -14, f'\u00d8{BASE_DIA}', fs=9)

    # Alturas (verticais) — lado esquerdo: rosca e total
    dim_v(ax1, rod_bottom, y_top, cx, -50, f'{ROD_LENGTH}', fs=8)
    dim_v(ax1, rub_bottom, y_top, cx, -62, f'{TOTAL_FOOT}\n(total)', fs=7)

    # Alturas (verticais) — lado direito: colar, chanfro, base, borracha
    dim_v(ax1, collar_bottom, rod_bottom, cx + COLLAR_R, 10, f'{COLLAR_H}', fs=8, color=ORANGE)
    dim_v(ax1, chamfer_bottom, collar_bottom, cx + BASE_R, 10, f'{CHAMFER_H}', fs=8)
    dim_v(ax1, base_bottom, chamfer_bottom, cx + BASE_R, 10, f'{BASE_H}', fs=8)
    dim_v(ax1, rub_bottom, base_bottom, cx + BASE_R, 10, f'{RUBBER_H:.0f}', fs=7)

    # Angulo do chanfro
    angle_ch = np.degrees(np.arctan2(CHAMFER_H, BASE_R - COLLAR_R))
    ax1.text(cx - BASE_R + 14, (collar_bottom + chamfer_bottom) / 2 - 2,
             f'~{angle_ch:.0f}\u00b0', fontsize=7, color=ORANGE,
             fontweight='bold', ha='center')

    # Anotacoes de texto — posicionadas sem sobrepor cotas
    ax1.text(cx + ROD_R + 10, y_top - ROD_LENGTH / 2,
             'Rosca\nM12\u00d71,75', fontsize=7, va='center', fontweight='bold')

    ax1.text(cx + COLLAR_R + 22, collar_bottom + COLLAR_H / 2,
             u'COLAR (batente)', fontsize=6.5, color=ORANGE,
             fontweight='bold', va='center')

    ax1.text(cx, rub_bottom - 15,
             u'Borracha neoprene \u00d860mm\u00d71mm\n(colada ap\u00f3s usinagem)',
             ha='center', fontsize=6, color='#666')

    ax1.set_xlim(cx - 75, cx + 85)
    ax1.set_ylim(rub_bottom - 22, y_top + 18)
    ax1.set_aspect('equal')
    clean_axes(ax1)

    # === VISTA FRONTAL ===
    ax2 = fig.add_axes([0.52, 0.55, 0.20, 0.38])
    ax2.set_title('VISTA FRONTAL\n(perfil externo)', fontsize=9,
                  fontweight='bold', pad=5, color=DARK)

    cx2 = 30
    for side in [-1, 1]:
        ax2.plot([cx2 + side * ROD_R, cx2 + side * ROD_R], [y_top, rod_bottom], color=pe_c, lw=1.5)
        ax2.plot([cx2 + side * ROD_R, cx2 + side * COLLAR_R], [rod_bottom, rod_bottom], color=pe_c, lw=1.5)
        ax2.plot([cx2 + side * COLLAR_R, cx2 + side * COLLAR_R], [rod_bottom, collar_bottom], color=pe_c, lw=1.5)
        ax2.plot([cx2 + side * COLLAR_R, cx2 + side * BASE_R], [collar_bottom, chamfer_bottom], color=pe_c, lw=1.5)
        ax2.plot([cx2 + side * BASE_R, cx2 + side * BASE_R], [chamfer_bottom, base_bottom], color=pe_c, lw=1.5)
    ax2.plot([cx2 - ROD_R, cx2 + ROD_R], [y_top, y_top], color=pe_c, lw=1.5)
    ax2.plot([cx2 - BASE_R, cx2 + BASE_R], [base_bottom, base_bottom], color=pe_c, lw=1.5)
    ax2.plot([cx2 - BASE_R, cx2 + BASE_R], [rub_bottom, rub_bottom], color='#444', lw=1)
    ax2.plot([cx2, cx2], [y_top + 3, rub_bottom - 3], color='#BBB', lw=0.5, ls='-.')

    ax2.set_xlim(cx2 - 40, cx2 + 40)
    ax2.set_ylim(rub_bottom - 10, y_top + 10)
    ax2.set_aspect('equal')
    clean_axes(ax2)

    # === VISTA INFERIOR ===
    ax3 = fig.add_axes([0.73, 0.55, 0.23, 0.38])
    ax3.set_title('VISTA INFERIOR', fontsize=9, fontweight='bold', pad=5, color=DARK)

    outer = plt.Circle((0, 0), BASE_R, fc='#E0E0E0', ec=pe_c, lw=1.5, zorder=2)
    ax3.add_patch(outer)
    center = plt.Circle((0, 0), ROD_R, fc='#BBB', ec=pe_c, lw=1, zorder=3)
    ax3.add_patch(center)
    ax3.plot([-BASE_R - 3, BASE_R + 3], [0, 0], color='#999', lw=0.5, ls='-.')
    ax3.plot([0, 0], [-BASE_R - 3, BASE_R + 3], color='#999', lw=0.5, ls='-.')

    ax3.annotate('', xy=(-BASE_R, -18), xytext=(BASE_R, -18),
                 arrowprops=dict(arrowstyle='<->', color=DARK, lw=0.8))
    ax3.text(0, -22, f'\u00d8{BASE_DIA}', ha='center', va='top', fontsize=9,
             color=DARK, fontweight='bold')
    ax3.text(0, BASE_R + 5, 'Borracha 1mm\n(colada)', ha='center', fontsize=6, color='#666')

    ax3.set_xlim(-38, 38)
    ax3.set_ylim(-32, 38)
    ax3.set_aspect('equal')
    clean_axes(ax3)

    # === TABELA ===
    ax4 = fig.add_axes([0.52, 0.17, 0.44, 0.32])
    ax4.set_title(u'ESPECIFICA\u00c7\u00d5ES DA PE\u00c7A', fontsize=9,
                  fontweight='bold', pad=5, color=DARK)
    ax4.axis('off')

    angle_ch = np.degrees(np.arctan2(CHAMFER_H, BASE_R - COLLAR_R))
    specs = [
        [u'Par\u00e2metro', 'Valor'],
        ['Tipo', u'Pe\u00e7a torneada (torno mec\u00e2nico)'],
        ['Rosca', f'M12\u00d71,75 \u2014 \u00d8{ROD_DIA}mm, {ROD_LENGTH}mm comprimento'],
        ['Colar', f'\u00d8{COLLAR_DIA}mm, {COLLAR_H}mm altura (batente)'],
        ['Chanfro', f'\u00d8{COLLAR_DIA}\u2192\u00d8{BASE_DIA}, {CHAMFER_H}mm (~{angle_ch:.0f}\u00b0)'],
        ['Base', f'\u00d8{BASE_DIA}mm, {BASE_H}mm espessura'],
        ['Borracha', f'\u00d8{BASE_DIA}mm, {RUBBER_H:.0f}mm neoprene (colar ap\u00f3s usinagem)'],
        ['Material', u'A\u00e7o carbono ou inox (barra \u00d860mm)'],
        ['Altura total', f'{TOTAL_FOOT}mm (rosca+colar+chanfro+base+borracha)'],
    ]

    table = ax4.table(cellText=specs[1:], colLabels=specs[0],
                      loc='center', cellLoc='left')
    table.auto_set_font_size(False)
    table.set_fontsize(7)
    table.scale(1, 1.3)
    for j in range(2):
        table[0, j].set_facecolor(ORANGE)
        table[0, j].set_text_props(color='white', fontweight='bold')
    for i in range(1, len(specs)):
        table[i, 0].set_text_props(fontweight='bold')
        color = '#F8F8F8' if i % 2 == 0 else 'white'
        for j in range(2):
            table[i, j].set_facecolor(color)

    add_title_block(fig, 'P\u00e9 torneado com colar',
                    u'A\u00e7o carbono/inox (barra \u00d860mm)',
                    'Ver cotas', '4 unidades',
                    u'Borracha colada ap\u00f3s usinagem')

    fig.savefig(f'{OUT_DIR}/fab_pezinho.pdf', bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print("  -> fab_pezinho.pdf")


# =============================================================================
# 4. JUNTA DE ACO
# =============================================================================

def draw_junta():
    fig = plt.figure(figsize=(14, 10))

    # === VISTA SUPERIOR ===
    ax1 = fig.add_axes([0.05, 0.25, 0.45, 0.68])
    ax1.set_title('VISTA SUPERIOR', fontsize=10, fontweight='bold', pad=8, color=DARK)

    junta = patches.Rectangle((0, 0), GASKET_L, GASKET_W, lw=2,
                                ec='black', fc=LIGHT_GRAY)
    ax1.add_patch(junta)

    cx_j = GASKET_L / 2
    cy_j = GASKET_W / 2
    hole_offset = HOLE_SPACING / 2
    h1 = (cx_j - hole_offset, cy_j)
    h2 = (cx_j + hole_offset, cy_j)

    draw_hole(ax1, h1[0], h1[1], HOLE_DIA)
    draw_hole(ax1, h2[0], h2[1], HOLE_DIA)

    ax1.plot([cx_j, cx_j], [-3, GASKET_W + 3], color='#CCC', lw=0.5, ls='-.')
    ax1.plot([-3, GASKET_L + 3], [cy_j, cy_j], color='#CCC', lw=0.5, ls='-.')

    dim_h(ax1, 0, GASKET_L, 0, -10, f'{GASKET_L}', fs=9)
    dim_v(ax1, 0, GASKET_W, 0, -12, f'{GASKET_W}', fs=9)
    dim_h(ax1, 0, h1[0], h1[1], 12, f'{h1[0]:.1f}', fs=7)
    dim_h(ax1, h1[0], h2[0], h1[1], -10, f'{HOLE_SPACING}', fs=8, color=ORANGE)
    dim_v(ax1, 0, h1[1], h2[0], 8, f'{cy_j:.0f}', fs=7)

    ax1.text(h2[0] + 10, h2[1], f'\u00d8{HOLE_DIA} pass.',
             fontsize=7, color=DARK, va='center',
             bbox=dict(fc='white', ec='#DDD', pad=1.5, boxstyle='round,pad=0.3'))

    ax1.set_xlim(-18, GASKET_L + 20)
    ax1.set_ylim(-18, GASKET_W + 18)
    ax1.set_aspect('equal')
    clean_axes(ax1)

    # === VISTA FRONTAL ===
    ax2 = fig.add_axes([0.55, 0.55, 0.40, 0.35])
    ax2.set_title('VISTA FRONTAL', fontsize=9, fontweight='bold', pad=5, color=DARK)

    profile = patches.Rectangle((0, 0), GASKET_L, GASKET_T, lw=2,
                                 ec='black', fc=LIGHT_GRAY)
    ax2.add_patch(profile)
    dim_v(ax2, 0, GASKET_T, 0, -8, f'{GASKET_T}', fs=9)
    dim_h(ax2, 0, GASKET_L, 0, -4, f'{GASKET_L}', fs=8)
    for hx in [h1[0], h2[0]]:
        ax2.plot([hx - 3, hx + 3], [GASKET_T, GASKET_T], color='black', lw=1.5)
        ax2.plot([hx, hx], [0, GASKET_T], color='#CCC', lw=0.3, ls=':')

    ax2.set_xlim(-12, GASKET_L + 8)
    ax2.set_ylim(-8, GASKET_T + 8)
    ax2.set_aspect('equal')
    clean_axes(ax2)

    # === NOTA FUNCIONAL ===
    ax3 = fig.add_axes([0.55, 0.17, 0.40, 0.32])
    ax3.set_title(u'FUN\u00c7\u00c3O DA PE\u00c7A', fontsize=9,
                  fontweight='bold', pad=5, color=DARK)
    ax3.axis('off')

    specs = [
        [u'Par\u00e2metro', 'Valor'],
        [u'Fun\u00e7\u00e3o', u'Distribuir carga entre c\u00e9lula e chapa'],
        ['Material', u'A\u00e7o (mais duro que alum\u00ednio)'],
        [u'Posi\u00e7\u00e3o', u'Entre chapa superior e c\u00e9lula de carga'],
        ['Furos', f'2\u00d7 \u00d8{HOLE_DIA}mm passante, {HOLE_SPACING}mm entre centros'],
        ['Acabamento', u'Superf\u00edcies planas, sem rebarbas'],
    ]

    table = ax3.table(cellText=specs[1:], colLabels=specs[0],
                      loc='center', cellLoc='left')
    table.auto_set_font_size(False)
    table.set_fontsize(7.5)
    table.scale(1, 1.5)
    for j in range(2):
        table[0, j].set_facecolor(ORANGE)
        table[0, j].set_text_props(color='white', fontweight='bold')
    for i in range(1, len(specs)):
        table[i, 0].set_text_props(fontweight='bold')
        color = '#F8F8F8' if i % 2 == 0 else 'white'
        for j in range(2):
            table[i, j].set_facecolor(color)

    add_title_block(fig, u'Junta de a\u00e7o', u'A\u00e7o carbono',
                    f'{GASKET_T}mm', '4 unidades',
                    u'Impede esmagamento do alum\u00ednio')

    fig.savefig(f'{OUT_DIR}/fab_junta.pdf', bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print("  -> fab_junta.pdf")


# =============================================================================
# 5. VISTA EXPLODIDA DE MONTAGEM
# =============================================================================

def draw_montagem():
    fig = plt.figure(figsize=(14, 10))

    ax = fig.add_axes([0.05, 0.15, 0.58, 0.80])
    ax.set_title(u'VISTA EXPLODIDA DE MONTAGEM',
                 fontsize=11, fontweight='bold', pad=10, color=DARK)

    cx = 50            # centro X
    cx2 = 130          # segunda coluna (tubo)
    gap = 16
    pc = '#D0D0D0'
    pe_c = '#555'

    # Dimensoes visuais
    bolt_shank_w = 8
    bolt_shank_h = 28
    bolt_head_h = 4
    bolt_head_w = 18

    top_h = 12
    top_w = 80

    gasket_h = 5
    gasket_w = 36

    cell_h = 24
    cell_w = 42

    tube_h = 24         # tubo visual (mesma altura que celula)
    tube_w = 24
    tube_wall_v = 3     # parede visual

    bot_h = 6
    bot_w = 70

    nut_h = 5
    nut_w = 20

    # Posicoes Y (de cima pra baixo)
    y_bolt_top = 270
    y_bolt = y_bolt_top - bolt_head_h - bolt_shank_h

    y_top = y_bolt - gap
    y_gasket = y_top - top_h - gap
    y_cell = y_gasket - gasket_h - gap
    y_bot = y_cell - cell_h - gap
    y_nut = y_bot - bot_h - gap

    # Tubo — mesma altura que celula+junta, entre as chapas
    y_tube = y_cell

    # Pe
    foot_rod_h = 20
    foot_collar_h = 4
    foot_chamfer_h = 5
    foot_base_h = 7
    foot_rubber_h = 2
    foot_total = foot_rod_h + foot_collar_h + foot_chamfer_h + foot_base_h + foot_rubber_h
    y_foot_top = y_nut - nut_h - gap
    y_foot_bot = y_foot_top - foot_total

    def draw_rect(x_center, y, h, w, fc=pc):
        r = patches.Rectangle((x_center - w / 2, y), w, h, lw=1.5, ec=pe_c, fc=fc, zorder=2)
        ax.add_patch(r)

    # =====================================================
    # COLUNA ESQUERDA — EMPILHAMENTO DO CANTO (1 de 4)
    # =====================================================

    ax.text(cx, y_bolt_top + 12, u'CANTO (t\u00edpico, \u00d74)',
            ha='center', fontsize=8, fontweight='bold', color=DARK)

    # 1. Parafuso
    draw_rect(cx, y_bolt, bolt_shank_h, bolt_shank_w, fc='#AAA')
    head = Polygon([
        (cx - bolt_head_w / 2, y_bolt + bolt_shank_h + bolt_head_h),
        (cx + bolt_head_w / 2, y_bolt + bolt_shank_h + bolt_head_h),
        (cx + bolt_shank_w / 2, y_bolt + bolt_shank_h),
        (cx - bolt_shank_w / 2, y_bolt + bolt_shank_h),
    ], closed=True, lw=1, ec=pe_c, fc='#999', zorder=2)
    ax.add_patch(head)
    ax.plot([cx - 2, cx + 2], [y_bolt + bolt_shank_h + bolt_head_h - 1.5,
            y_bolt + bolt_shank_h + bolt_head_h - 1.5], color='#666', lw=1.5)
    ax.text(cx - bolt_head_w / 2 - 3, y_bolt + bolt_shank_h,
            u'Parafuso Allen\nM10\u00d750\nDIN 7991',
            fontsize=5.5, va='center', fontweight='bold', color=DARK, ha='right')

    # 2. Chapa superior (com escareamento)
    draw_rect(cx, y_top, top_h, top_w)
    cs_visual = (5.5 / 6.0) * top_h
    remaining = top_h - cs_visual
    cs_w = bolt_head_w / 2
    shank_hw = bolt_shank_w / 2 - 0.5
    ax.fill([cx - cs_w, cx + cs_w, cx + shank_hw, cx - shank_hw],
            [y_top + top_h, y_top + top_h, y_top + remaining, y_top + remaining],
            fc='white', ec='black', lw=0.8, zorder=3)
    ax.fill([cx - shank_hw, cx + shank_hw, cx + shank_hw, cx - shank_hw],
            [y_top + remaining, y_top + remaining, y_top, y_top],
            fc='white', ec='black', lw=0.5, zorder=3)

    ax.text(cx + top_w / 2 + 3, y_top + top_h / 2,
            f'CHAPA SUPERIOR\n{TOP_W}\u00d7{TOP_H}\u00d7{TOP_THICK}mm\nR{CORNER_R}, escareado',
            fontsize=5, va='center', fontweight='bold', color=ORANGE)

    # 3. Junta
    draw_rect(cx, y_gasket, gasket_h, gasket_w, fc='#B8B8B8')
    for hy in np.arange(y_gasket + 1, y_gasket + gasket_h, 1.5):
        ax.plot([cx - gasket_w / 2 + 2, cx + gasket_w / 2 - 2], [hy, hy],
                color='#888', lw=0.3, zorder=3)
    ax.text(cx + gasket_w / 2 + 3, y_gasket + gasket_h / 2,
            f'JUNTA A\u00c7O\n{GASKET_L}\u00d7{GASKET_W}\u00d7{GASKET_T}mm',
            fontsize=5, va='center', fontweight='bold', color=DARK)

    # 4. Celula de carga
    draw_rect(cx, y_cell, cell_h, cell_w, fc='#E8D8C0')
    ax.plot([cx - cell_w / 2 + 3, cx + cell_w / 2 - 3],
            [y_cell + cell_h / 2, y_cell + cell_h / 2],
            color='#C0A880', lw=0.5, ls='--')
    ax.text(cx + cell_w / 2 + 3, y_cell + cell_h / 2,
            u'C\u00c9LULA DE CARGA\nDYX-301 500kg',
            fontsize=5, va='center', fontweight='bold', color=DARK)
    ax.plot([cx - 3, cx + 3], [y_cell + 2, y_cell + 2], color='#666', lw=1)

    # 5. Chapa inferior
    draw_rect(cx, y_bot, bot_h, bot_w)
    ax.text(cx + bot_w / 2 + 3, y_bot + bot_h / 2,
            f'CHAPA INFERIOR\n{BOT_W}\u00d7{BOT_H}\u00d7{BOT_THICK}mm\nchanfro {BOT_CHAMFER}\u00d7{BOT_CHAMFER}',
            fontsize=5, va='center', fontweight='bold', color=ORANGE)

    # 6. Porca + arruela
    draw_rect(cx, y_nut + nut_h - 1.5, 1.5, nut_w + 4, fc='#BBB')
    draw_rect(cx, y_nut, nut_h - 1.5, nut_w, fc='#AAA')
    ax.text(cx + nut_w / 2 + 5, y_nut + nut_h / 2,
            'PORCA M10\n+ arruela', fontsize=5, va='center', fontweight='bold', color=DARK)

    # 7. Pe com colar
    y_ft = y_foot_top
    draw_rect(cx, y_ft - foot_rod_h, foot_rod_h, 8)
    draw_rect(cx, y_ft - foot_rod_h - foot_collar_h, foot_collar_h, 14, fc='#C0C0C0')
    y_ch_top = y_ft - foot_rod_h - foot_collar_h
    y_ch_bot = y_ch_top - foot_chamfer_h
    ch = Polygon([
        (cx - 7, y_ch_top), (cx + 7, y_ch_top),
        (cx + 16, y_ch_bot), (cx - 16, y_ch_bot),
    ], closed=True, lw=1, ec=pe_c, fc=pc, zorder=2)
    ax.add_patch(ch)
    draw_rect(cx, y_ch_bot - foot_base_h, foot_base_h, 32)
    draw_rect(cx, y_ch_bot - foot_base_h - foot_rubber_h, foot_rubber_h, 32, fc='#444')
    ax.text(cx - 20, y_ft - foot_total / 2,
            f'P\u00c9 TORNEADO\ncom colar\n\u00d8{BASE_DIA}mm',
            fontsize=5, va='center', fontweight='bold', color=DARK, ha='right')

    # Linhas de ligacao (coluna canto)
    for y_from, y_to in [
        (y_bolt, y_top + top_h), (y_top, y_gasket + gasket_h),
        (y_gasket, y_cell + cell_h), (y_cell, y_bot + bot_h),
        (y_bot, y_nut + nut_h), (y_nut, y_ft),
    ]:
        ax.plot([cx, cx], [y_to, y_from], color='#BBB', lw=0.8, ls=':', zorder=1)

    # =====================================================
    # COLUNA DIREITA — TUBO DE REFORCO (1 de 2)
    # =====================================================

    ax.text(cx2, y_bolt_top + 12, u'REFOR\u00c7O (t\u00edpico, \u00d72)',
            ha='center', fontsize=8, fontweight='bold', color=ORANGE)

    # Chapa superior (repetida, mais estreita)
    draw_rect(cx2, y_top, top_h, 55)
    ax.text(cx2, y_top + top_h / 2, 'chapa sup.',
            ha='center', va='center', fontsize=5, color='#666')

    # Tubo quadrado de aço (entre as chapas)
    # Exterior
    draw_rect(cx2, y_tube, tube_h, tube_w, fc='#B0B8C0')
    # Interior (oco)
    inner = patches.Rectangle(
        (cx2 - tube_w / 2 + tube_wall_v, y_tube + tube_wall_v),
        tube_w - 2 * tube_wall_v, tube_h - 2 * tube_wall_v,
        lw=0.8, ec=pe_c, fc='#D0D4D8', zorder=3)
    ax.add_patch(inner)

    ax.text(cx2 + tube_w / 2 + 5, y_tube + tube_h / 2,
            u'TUBO QUADRADO A\u00c7O\n35\u00d735\u00d72mm\n527mm compr.\ncolado com ep\u00f3xi',
            fontsize=5.5, va='center', fontweight='bold', color='#2266AA')

    # Indicacao de cola
    ax.plot([cx2 - tube_w / 2, cx2 + tube_w / 2],
            [y_tube + tube_h, y_tube + tube_h], color=ORANGE, lw=2, zorder=4)
    ax.plot([cx2 - tube_w / 2, cx2 + tube_w / 2],
            [y_tube, y_tube], color=ORANGE, lw=2, zorder=4)
    ax.text(cx2 + tube_w / 2 + 5, y_tube + tube_h + 2,
            u'cola ep\u00f3xi', fontsize=4.5, color=ORANGE, va='center')
    ax.text(cx2 + tube_w / 2 + 5, y_tube - 2,
            u'cola ep\u00f3xi', fontsize=4.5, color=ORANGE, va='center')

    # Chapa inferior (repetida)
    draw_rect(cx2, y_bot, bot_h, 50)
    ax.text(cx2, y_bot + bot_h / 2, 'chapa inf.',
            ha='center', va='center', fontsize=5, color='#666')

    # Linhas de ligacao (coluna tubo)
    ax.plot([cx2, cx2], [y_top, y_tube + tube_h], color='#BBB', lw=0.8, ls=':', zorder=1)
    ax.plot([cx2, cx2], [y_bot + bot_h, y_tube], color='#BBB', lw=0.8, ls=':', zorder=1)

    # Seta de montagem (canto)
    floor_y = y_ch_bot - foot_base_h - foot_rubber_h - 5
    ax.annotate('', xy=(cx - 50, floor_y), xytext=(cx - 50, y_bolt_top + 5),
                arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2))

    # Piso
    ax.plot([cx - 45, cx + 45], [floor_y, floor_y], color='#999', lw=1.5, ls='-')
    ax.text(cx, floor_y - 4, u'PISO', fontsize=5, ha='center', color='#999')

    ax.set_xlim(-20, 185)
    ax.set_ylim(floor_y - 10, y_bolt_top + 22)
    ax.set_aspect('equal')
    clean_axes(ax)

    # === SEQUENCIA DE MONTAGEM ===
    ax2 = fig.add_axes([0.60, 0.18, 0.37, 0.72])
    ax2.set_title(u'SEQU\u00caNCIA DE MONTAGEM', fontsize=10, fontweight='bold',
                  pad=8, color=DARK)
    ax2.axis('off')

    steps = [
        ('1', u'Colar 2 tubos de a\u00e7o na face interna\nda chapa superior (Y=194 e Y=306mm)\nLixar + ep\u00f3xi + prensar 24h'),
        ('2', u'Inserir parafusos Allen M10 DIN 7991\npelo lado escareado da chapa superior'),
        ('3', u'Posicionar juntas de a\u00e7o sobre as\nc\u00e9lulas de carga'),
        ('4', u'Encaixar c\u00e9lulas nos parafusos\n(2 parafusos por c\u00e9lula, 4 cantos)'),
        ('5', u'Colar tubos de a\u00e7o na chapa inferior (ep\u00f3xi)\ne posicionar sobre os parafusos'),
        ('6', u'Fixar com porca M10 + arruela\n(n\u00e3o apertar totalmente ainda)'),
        ('7', u'Rosquear p\u00e9s (M12\u00d71,75)\nat\u00e9 o colar encostar na c\u00e9lula'),
        ('8', u'Nivelar (n\u00edvel de bolha) e apertar\nporcas. Testar rigidez sob carga'),
    ]

    y_start = 0.95
    for i, (num, text) in enumerate(steps):
        y_pos = y_start - i * 0.112
        ax2.text(0.02, y_pos, num, fontsize=11, fontweight='bold', color='white',
                 va='top', transform=ax2.transAxes,
                 bbox=dict(fc=ORANGE, ec='none', pad=3, boxstyle='circle,pad=0.3'))
        ax2.text(0.10, y_pos, text, fontsize=6.5, va='top', color=DARK,
                 transform=ax2.transAxes)

    ax2.text(0.02, 0.02,
             u'NOTA: 4 cantos \u00d7 (2 paraf. + 1 junta + 1 c\u00e9lula + 1 p\u00e9)\n'
             u'+ 2 tubos quadrados de a\u00e7o colados (refor\u00e7o central)\n'
             u'Total: 8 paraf. M10, 4 juntas, 4 c\u00e9lulas, 4 p\u00e9s, 2 tubos a\u00e7o',
             fontsize=6, color=MID_GRAY, transform=ax2.transAxes,
             va='bottom', style='italic')

    add_title_block(fig, 'Montagem', 'Conjunto completo',
                    'N/A', u'Refer\u00eancia',
                    u'Parafusos DIN 7991 M10 escareados')

    fig.savefig(f'{OUT_DIR}/fab_montagem.pdf', bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print("  -> fab_montagem.pdf")


# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    print("Gerando desenhos de fabricacao...")
    print("=" * 50)

    draw_chapa_superior()
    draw_chapa_inferior()
    draw_pezinho()
    draw_junta()
    draw_montagem()

    print(f"\n\u2713 5 PDFs gerados em {OUT_DIR}/")
    print(f"  fab_chapa_superior.pdf  \u2014 cantos R{CORNER_R}, furos escareados M10")
    print(f"  fab_chapa_inferior.pdf  \u2014 chanfro {BOT_CHAMFER}\u00d7{BOT_CHAMFER}, furos \u00d8{HOLE_DIA}")
    print(f"  fab_pezinho.pdf         \u2014 com colar \u00d8{COLLAR_DIA}\u00d7{COLLAR_H}mm")
    print(f"  fab_junta.pdf           \u2014 furos \u00d8{HOLE_DIA}")
    print(f"  fab_montagem.pdf        \u2014 vista explodida + sequencia")
