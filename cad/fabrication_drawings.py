"""
Force Plate MVP — Fabrication Drawings
Nova O2 Sports Science

Generates 3 PDFs for fabrication (1 per piece):
1. fab_chapa_superior.pdf — Top plate 600×500mm, 6mm aluminum
2. fab_chapa_inferior.pdf — Bottom plate 527×396mm, 3mm aluminum
3. fab_pezinho.pdf — Turned foot piece (×4)

Each PDF: 3 views + title block with Nova O2 branding.
No assembly context — just the piece the fabricator needs to make.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Polygon, FancyBboxPatch
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
import numpy as np
from datetime import date

# =============================================================================
# CONSTANTS
# =============================================================================

ICON_PATH = '/workspace/03-engineering/nova-o2/force-plate/cad/nova_o2_icon.png'
ORANGE = '#E8820C'
DARK = '#333333'
LIGHT_GRAY = '#F0F0F0'
TODAY = date.today().strftime('%Y-%m-%d')

# Hole coordinates (from plate_drawing.py calculations)
# Origin: bottom-left corner of top plate
HOLES = {
    'C1': [(56.7, 428.1), (68.3, 406.0)],
    'C2': [(543.3, 428.1), (531.7, 406.0)],
    'C3': [(56.7, 71.9), (68.3, 94.0)],
    'C4': [(543.3, 71.9), (531.7, 94.0)],
}

# Bottom plate offset (centered under top plate)
TOP_W, TOP_H = 600, 500
BOT_W, BOT_H = 527, 396
BOT_X0 = (TOP_W - BOT_W) / 2
BOT_Y0 = (TOP_H - BOT_H) / 2

# Foot dimensions
ROD_DIA = 12
ROD_LENGTH = 30
CHAMFER_H = 6
BASE_DIA = 60
BASE_H = 5
RUBBER_H = 1
BASE_R = BASE_DIA / 2
ROD_R = ROD_DIA / 2


# =============================================================================
# TITLE BLOCK
# =============================================================================

def add_title_block(fig, piece_name, material, thickness, quantity, notes=""):
    """Add branded title block at bottom of figure."""
    # Title block area
    ax_tb = fig.add_axes([0.0, 0.0, 1.0, 0.12])
    ax_tb.set_xlim(0, 100)
    ax_tb.set_ylim(0, 12)
    ax_tb.axis('off')

    # Orange bar background
    bar = FancyBboxPatch((0, 0), 100, 12, boxstyle="square,pad=0",
                          fc=ORANGE, ec='none', zorder=1)
    ax_tb.add_patch(bar)

    # Logo
    try:
        logo = mpimg.imread(ICON_PATH)
        im = OffsetImage(logo, zoom=0.035)
        ab = AnnotationBbox(im, (3, 6), frameon=False, zorder=3)
        ax_tb.add_artist(ab)
    except:
        pass

    # Text
    ax_tb.text(7, 8.5, 'NOVA O2 SPORTS SCIENCE', fontsize=9, fontweight='bold',
               color='white', va='center', zorder=2)
    ax_tb.text(7, 5.5, f'DESENHO DE FABRICAÇÃO', fontsize=7,
               color='white', va='center', zorder=2, alpha=0.9)
    ax_tb.text(7, 3, f'Projeto: Force Plate MVP', fontsize=6,
               color='white', va='center', zorder=2, alpha=0.8)

    # Piece info (right side)
    info_x = 45
    ax_tb.text(info_x, 10, f'Peça:', fontsize=6, color='white', alpha=0.7, va='center')
    ax_tb.text(info_x + 5, 10, f'{piece_name}', fontsize=8, fontweight='bold',
               color='white', va='center')
    ax_tb.text(info_x, 7.5, f'Material:', fontsize=6, color='white', alpha=0.7, va='center')
    ax_tb.text(info_x + 7, 7.5, f'{material}', fontsize=7, color='white', va='center')
    ax_tb.text(info_x, 5, f'Espessura:', fontsize=6, color='white', alpha=0.7, va='center')
    ax_tb.text(info_x + 8, 5, f'{thickness}', fontsize=7, color='white', va='center')
    ax_tb.text(info_x, 2.5, f'Quantidade:', fontsize=6, color='white', alpha=0.7, va='center')
    ax_tb.text(info_x + 9, 2.5, f'{quantity}', fontsize=7, fontweight='bold',
               color='white', va='center')

    # Date and notes (far right)
    ax_tb.text(85, 10, f'Data: {TODAY}', fontsize=6, color='white', alpha=0.7, va='center')
    ax_tb.text(85, 7.5, f'Cotas em mm', fontsize=6, color='white', alpha=0.7, va='center')
    ax_tb.text(85, 5, f'Escala: indicada', fontsize=6, color='white', alpha=0.7, va='center')
    if notes:
        ax_tb.text(85, 2.5, notes, fontsize=5, color='white', alpha=0.7, va='center')

    # Separator line
    ax_tb.plot([0, 100], [12, 12], color=DARK, lw=1.5)


def dim(ax, p1, p2, offset, text, horiz=True, fs=7, color='#333'):
    """Dimension line."""
    if horiz:
        y = p1[1] + offset
        ax.annotate('', xy=(p1[0], y), xytext=(p2[0], y),
                    arrowprops=dict(arrowstyle='<->', color=color, lw=0.7))
        ax.text((p1[0]+p2[0])/2, y + (3 if offset > 0 else -3), text,
                ha='center', va='bottom' if offset > 0 else 'top', fontsize=fs, color=color)
        ax.plot([p1[0], p1[0]], [p1[1], y], color='#999', lw=0.3, ls='--')
        ax.plot([p2[0], p2[0]], [p2[1], y], color='#999', lw=0.3, ls='--')
    else:
        x = p1[0] + offset
        ax.annotate('', xy=(x, p1[1]), xytext=(x, p2[1]),
                    arrowprops=dict(arrowstyle='<->', color=color, lw=0.7))
        ax.text(x + (3 if offset > 0 else -3), (p1[1]+p2[1])/2, text,
                ha='left' if offset > 0 else 'right', va='center',
                fontsize=fs, color=color, rotation=90)
        ax.plot([p1[0], x], [p1[1], p1[1]], color='#999', lw=0.3, ls='--')
        ax.plot([p2[0], x], [p2[1], p2[1]], color='#999', lw=0.3, ls='--')


def draw_hole(ax, x, y, dia=13, label=None):
    """Draw a hole with center marks."""
    c = plt.Circle((x, y), dia/2, fill=False, ec='black', lw=1, zorder=4)
    ax.add_patch(c)
    s = 4
    ax.plot([x-s, x+s], [y, y], color='black', lw=0.4, zorder=4)
    ax.plot([x, x], [y-s, y+s], color='black', lw=0.4, zorder=4)
    if label:
        ax.text(x, y + dia/2 + 3, label, ha='center', fontsize=5, color='#666')


# =============================================================================
# PLATE DRAWING (reusable for top and bottom)
# =============================================================================

def draw_plate_fabrication(filename, plate_w, plate_h, thickness, holes_coords,
                           piece_name, material, quantity, notes="",
                           is_top=True):
    """Generate fabrication PDF for a plate."""
    fig = plt.figure(figsize=(14, 10))

    # === VIEW 1: TOP VIEW (main) ===
    ax1 = fig.add_axes([0.05, 0.28, 0.55, 0.65])
    ax1.set_title('VISTA SUPERIOR', fontsize=10, fontweight='bold', pad=8)

    # Plate outline
    plate = patches.Rectangle((0, 0), plate_w, plate_h, lw=2,
                               ec='black', fc=LIGHT_GRAY, zorder=1)
    ax1.add_patch(plate)

    # If bottom plate, shift hole coordinates
    if not is_top:
        x_off = BOT_X0
        y_off = BOT_Y0
    else:
        x_off = 0
        y_off = 0

    # Draw all holes with coordinates
    hole_num = 1
    for cell_name in ['C1', 'C2', 'C3', 'C4']:
        for hx, hy in holes_coords[cell_name]:
            px = hx - x_off if not is_top else hx
            py = hy - y_off if not is_top else hy
            draw_hole(ax1, px, py, 13, f'F{hole_num}')

            # Coordinate labels
            ax1.text(px + 10, py, f'({px:.1f}, {py:.1f})',
                    fontsize=5, color='#666', va='center')
            hole_num += 1

    # Overall dimensions
    dim(ax1, (0, 0), (plate_w, 0), -30, f'{plate_w:.0f}', fs=9)
    dim(ax1, (0, 0), (0, plate_h), -30, f'{plate_h:.0f}', horiz=False, fs=9)

    # Reference corner
    ax1.plot(0, 0, 'o', color=ORANGE, ms=6, zorder=5)
    ax1.text(5, -15, 'ORIGEM\n(0,0)', fontsize=6, color=ORANGE, fontweight='bold')

    # Center line (for reference)
    ax1.plot([plate_w/2, plate_w/2], [-5, plate_h+5], color='#CCC', lw=0.5, ls='-.')
    ax1.plot([-5, plate_w+5], [plate_h/2, plate_h/2], color='#CCC', lw=0.5, ls='-.')

    ax1.set_xlim(-50, plate_w + 80)
    ax1.set_ylim(-50, plate_h + 30)
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.1)
    ax1.set_xlabel('X (mm)')
    ax1.set_ylabel('Y (mm)')

    # === VIEW 2: FRONT VIEW (side profile) ===
    ax2 = fig.add_axes([0.65, 0.55, 0.30, 0.30])
    ax2.set_title('VISTA FRONTAL', fontsize=9, fontweight='bold', pad=5)

    # Side profile
    profile = patches.Rectangle((0, 0), plate_w, thickness, lw=2,
                                  ec='black', fc=LIGHT_GRAY, zorder=1)
    ax2.add_patch(profile)

    # Thickness dimension
    dim(ax2, (0, 0), (0, thickness), -20, f'{thickness}mm', horiz=False, fs=8)
    dim(ax2, (0, 0), (plate_w, 0), -5, f'{plate_w:.0f}', fs=7)

    # Hole indications (as dashes on top surface)
    for cell_name in ['C1', 'C2', 'C3', 'C4']:
        for hx, hy in holes_coords[cell_name]:
            px = hx - x_off if not is_top else hx
            ax2.plot([px-3, px+3], [thickness, thickness], color='black', lw=1.5)
            ax2.plot([px, px], [0, thickness], color='#999', lw=0.3, ls=':')

    ax2.set_xlim(-30, plate_w + 20)
    ax2.set_ylim(-10, thickness + 15)
    ax2.set_aspect('equal')
    ax2.grid(True, alpha=0.1)

    # === VIEW 3: HOLE DETAIL ===
    ax3 = fig.add_axes([0.65, 0.18, 0.30, 0.32])
    ax3.set_title('DETALHE — Par de furos\n(típico, ×4)', fontsize=9, fontweight='bold', pad=5)

    # Zoom on one hole pair (C3)
    h1 = holes_coords['C3'][0]
    h2 = holes_coords['C3'][1]
    h1x = h1[0] - x_off if not is_top else h1[0]
    h1y = h1[1] - y_off if not is_top else h1[1]
    h2x = h2[0] - x_off if not is_top else h2[0]
    h2y = h2[1] - y_off if not is_top else h2[1]

    # Background
    margin = 25
    cx = (h1x + h2x) / 2
    cy = (h1y + h2y) / 2
    bg = patches.Rectangle((cx-margin, cy-margin), margin*2, margin*2,
                             lw=1, ec='#CCC', fc=LIGHT_GRAY, zorder=1)
    ax3.add_patch(bg)

    # Holes
    for hx, hy in [(h1x, h1y), (h2x, h2y)]:
        c = plt.Circle((hx, hy), 13/2, fill=False, ec='black', lw=1.5, zorder=4)
        ax3.add_patch(c)
        ax3.plot([hx-5, hx+5], [hy, hy], color='black', lw=0.5, zorder=4)
        ax3.plot([hx, hx], [hy-5, hy+5], color='black', lw=0.5, zorder=4)

    # Spacing dimension
    dist = np.sqrt((h2x-h1x)**2 + (h2y-h1y)**2)
    mid_x = (h1x + h2x) / 2
    mid_y = (h1y + h2y) / 2
    ax3.annotate('', xy=(h1x, h1y), xytext=(h2x, h2y),
                arrowprops=dict(arrowstyle='<->', color=ORANGE, lw=1))
    ax3.text(mid_x + 8, mid_y + 3, f'{dist:.1f}mm\n(entre centros)',
            fontsize=7, color=ORANGE, fontweight='bold')

    # Hole diameter
    ax3.text(h1x, h1y - 12, f'Ø13mm\npassante', ha='center', fontsize=6, color=DARK)

    ax3.set_xlim(cx - margin - 5, cx + margin + 15)
    ax3.set_ylim(cy - margin - 5, cy + margin + 5)
    ax3.set_aspect('equal')
    ax3.grid(True, alpha=0.1)

    # Title block
    add_title_block(fig, piece_name, material, f'{thickness}mm', quantity, notes)

    fig.savefig(filename, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"  → {filename}")


# =============================================================================
# FOOT DRAWING
# =============================================================================

def draw_foot_fabrication(filename):
    """Generate fabrication PDF for the turned foot."""
    fig = plt.figure(figsize=(14, 10))

    cx = 80  # center x for views

    # === VIEW 1: CROSS-SECTION (main) ===
    ax1 = fig.add_axes([0.05, 0.28, 0.45, 0.65])
    ax1.set_title('VISTA EM CORTE (seção longitudinal)', fontsize=10, fontweight='bold', pad=8)

    pc = '#D0D0D0'
    pe = '#444'

    # Reference line (top of rod)
    y_top = 100
    rod_bottom = y_top - ROD_LENGTH
    chamfer_top = rod_bottom
    chamfer_bottom = chamfer_top - CHAMFER_H
    base_top = chamfer_bottom
    base_bottom = base_top - BASE_H
    rub_bottom = base_bottom - RUBBER_H

    # Rod
    rod = patches.Rectangle((cx-ROD_R, rod_bottom), ROD_R*2, ROD_LENGTH,
                              lw=1, ec=pe, fc=pc, zorder=2)
    ax1.add_patch(rod)

    # Thread marks
    for ty in np.arange(y_top-1, rod_bottom+1, -2):
        ax1.plot([cx-ROD_R-1.5, cx+ROD_R+1.5], [ty, ty-1], color='#999', lw=0.3)

    # Chamfer (trapezoid)
    chamfer = Polygon([
        (cx-ROD_R, chamfer_top),
        (cx+ROD_R, chamfer_top),
        (cx+BASE_R, chamfer_bottom),
        (cx-BASE_R, chamfer_bottom),
    ], closed=True, lw=1, ec=pe, fc=pc, zorder=2)
    ax1.add_patch(chamfer)

    # Base disc
    base = patches.Rectangle((cx-BASE_R, base_bottom), BASE_R*2, BASE_H,
                               lw=1, ec=pe, fc=pc, zorder=2)
    ax1.add_patch(base)

    # Rubber
    rub = patches.Rectangle((cx-BASE_R, rub_bottom), BASE_R*2, RUBBER_H*2,
                              lw=0.8, ec='#222', fc='#444', zorder=2)
    ax1.add_patch(rub)

    # Center line
    ax1.plot([cx, cx], [y_top+5, rub_bottom-5], color='#999', lw=0.5, ls='-.')

    # === DIMENSIONS ===
    # Rod diameter
    dim(ax1, (cx-ROD_R, y_top-5), (cx+ROD_R, y_top-5), 8, f'Ø{ROD_DIA}', fs=8)

    # Rod length
    dim(ax1, (cx-40, y_top), (cx-40, rod_bottom), -5, f'{ROD_LENGTH}', horiz=False, fs=8)

    # Chamfer height
    dim(ax1, (cx+BASE_R+5, chamfer_top), (cx+BASE_R+5, chamfer_bottom),
        5, f'{CHAMFER_H}', horiz=False, fs=8)

    # Base diameter
    dim(ax1, (cx-BASE_R, rub_bottom), (cx+BASE_R, rub_bottom), -12, f'Ø{BASE_DIA}', fs=9)

    # Base height
    dim(ax1, (cx+BASE_R+5, base_top), (cx+BASE_R+5, base_bottom),
        5, f'{BASE_H}', horiz=False, fs=8)

    # Rubber
    dim(ax1, (cx-BASE_R-5, base_bottom), (cx-BASE_R-5, rub_bottom),
        -5, f'{RUBBER_H:.0f}', horiz=False, fs=7)

    # Total height
    total_h = ROD_LENGTH + CHAMFER_H + BASE_H + RUBBER_H
    dim(ax1, (cx-50, y_top), (cx-50, rub_bottom), -5, f'{total_h:.0f}\n(total)',
        horiz=False, fs=7)

    # Angle label
    ax1.text(cx-BASE_R+8, (chamfer_top+chamfer_bottom)/2,
            f'chanfro\n~{np.degrees(np.arctan2(CHAMFER_H, BASE_R-ROD_R)):.0f}°',
            fontsize=6, color=ORANGE, fontweight='bold', ha='center')

    # Thread spec
    ax1.text(cx+ROD_R+8, y_top-ROD_LENGTH/2,
            f'Rosca\nM12×1.75', fontsize=7, va='center', fontweight='bold')

    # Material note
    ax1.text(cx, rub_bottom-15, 'Borracha Ø60mm×1mm\n(colada após usinagem)',
            ha='center', fontsize=6, color='#666')

    ax1.set_xlim(cx-65, cx+75)
    ax1.set_ylim(rub_bottom-22, y_top+15)
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.1)

    # === VIEW 2: FRONT VIEW (external profile, no section) ===
    ax2 = fig.add_axes([0.52, 0.55, 0.20, 0.35])
    ax2.set_title('VISTA FRONTAL\n(perfil externo)', fontsize=9, fontweight='bold', pad=5)

    cx2 = 30

    # Rod (outline only)
    ax2.plot([cx2-ROD_R, cx2-ROD_R], [y_top, rod_bottom], color=pe, lw=1.5)
    ax2.plot([cx2+ROD_R, cx2+ROD_R], [y_top, rod_bottom], color=pe, lw=1.5)
    ax2.plot([cx2-ROD_R, cx2+ROD_R], [y_top, y_top], color=pe, lw=1.5)

    # Chamfer outline
    ax2.plot([cx2-ROD_R, cx2-BASE_R], [chamfer_top, chamfer_bottom], color=pe, lw=1.5)
    ax2.plot([cx2+ROD_R, cx2+BASE_R], [chamfer_top, chamfer_bottom], color=pe, lw=1.5)

    # Base outline
    ax2.plot([cx2-BASE_R, cx2-BASE_R], [base_top, base_bottom], color=pe, lw=1.5)
    ax2.plot([cx2+BASE_R, cx2+BASE_R], [base_top, base_bottom], color=pe, lw=1.5)
    ax2.plot([cx2-BASE_R, cx2+BASE_R], [base_bottom, base_bottom], color=pe, lw=1.5)

    # Rubber
    ax2.plot([cx2-BASE_R, cx2+BASE_R], [rub_bottom, rub_bottom], color='#444', lw=1)

    # Hidden lines (internal features)
    ax2.plot([cx2, cx2], [y_top+3, rub_bottom-3], color='#BBB', lw=0.5, ls='-.')

    ax2.set_xlim(cx2-40, cx2+40)
    ax2.set_ylim(rub_bottom-10, y_top+10)
    ax2.set_aspect('equal')
    ax2.grid(True, alpha=0.1)

    # === VIEW 3: BOTTOM VIEW ===
    ax3 = fig.add_axes([0.73, 0.55, 0.23, 0.35])
    ax3.set_title('VISTA INFERIOR', fontsize=9, fontweight='bold', pad=5)

    # Base circle (outer)
    outer = plt.Circle((0, 0), BASE_R, fc='#E0E0E0', ec=pe, lw=1.5, zorder=2)
    ax3.add_patch(outer)

    # Rubber indication
    rubber = plt.Circle((0, 0), BASE_R, fc='none', ec='#666', lw=0.5, ls='--', zorder=3)
    ax3.add_patch(rubber)

    # Center (rod base)
    center = plt.Circle((0, 0), ROD_R, fc='#BBB', ec=pe, lw=1, zorder=3)
    ax3.add_patch(center)

    # Center marks
    ax3.plot([-BASE_R-3, BASE_R+3], [0, 0], color='#999', lw=0.5, ls='-.')
    ax3.plot([0, 0], [-BASE_R-3, BASE_R+3], color='#999', lw=0.5, ls='-.')

    # Diameter
    ax3.annotate('', xy=(-BASE_R, -18), xytext=(BASE_R, -18),
                arrowprops=dict(arrowstyle='<->', color=DARK, lw=0.8))
    ax3.text(0, -22, f'Ø{BASE_DIA}', ha='center', va='top', fontsize=9,
            color=DARK, fontweight='bold')

    ax3.text(0, BASE_R + 5, 'Borracha 1mm\n(colada)', ha='center', fontsize=6, color='#666')

    ax3.set_xlim(-38, 38)
    ax3.set_ylim(-32, 38)
    ax3.set_aspect('equal')
    ax3.grid(True, alpha=0.1)

    # === SPEC TABLE ===
    ax4 = fig.add_axes([0.52, 0.18, 0.44, 0.32])
    ax4.set_title('ESPECIFICAÇÕES DA PEÇA', fontsize=9, fontweight='bold', pad=5)
    ax4.axis('off')

    specs = [
        ['Parâmetro', 'Valor'],
        ['Tipo', 'Peça torneada (torno mecânico)'],
        ['Rosca', f'M12×1.75, Ø{ROD_DIA}mm, {ROD_LENGTH}mm comprimento'],
        ['Chanfro', f'Ø{ROD_DIA}→Ø{BASE_DIA}, {CHAMFER_H}mm altura (~{np.degrees(np.arctan2(CHAMFER_H, BASE_R-ROD_R)):.0f}°)'],
        ['Base', f'Ø{BASE_DIA}mm, {BASE_H}mm espessura'],
        ['Borracha', f'Ø{BASE_DIA}mm, {RUBBER_H:.0f}mm neoprene (colar após usinagem)'],
        ['Material', 'Aço carbono ou inox (barra Ø60mm)'],
        ['Acabamento', 'Rosca M12×1.75 calibrada, superfície usinada'],
        ['Altura total', f'{total_h:.0f}mm (rosca + chanfro + base + borracha)'],
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

    # Title block
    add_title_block(fig, 'Pézinho torneado', 'Aço carbono/inox (barra Ø60mm)',
                    'Ver cotas', '4 unidades',
                    'Borracha colada após usinagem')

    fig.savefig(filename, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"  → {filename}")


# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    out = '/workspace/03-engineering/nova-o2/force-plate/cad'

    print("Gerando desenhos de fabricação...")
    print("=" * 50)

    # 1. Top plate
    draw_plate_fabrication(
        f'{out}/fab_chapa_superior.pdf',
        plate_w=TOP_W, plate_h=TOP_H, thickness=6,
        holes_coords=HOLES,
        piece_name='Chapa superior',
        material='Alumínio 6061-T6',
        quantity='1 unidade',
        notes='Acompanha 4 juntas aço\n56×32×2mm (2×Ø13, 25mm)',
        is_top=True
    )

    # 2. Bottom plate (shift hole coordinates)
    draw_plate_fabrication(
        f'{out}/fab_chapa_inferior.pdf',
        plate_w=BOT_W, plate_h=BOT_H, thickness=3,
        holes_coords=HOLES,
        piece_name='Chapa inferior',
        material='Alumínio',
        quantity='1 unidade',
        notes='Furos nas mesmas posições\nrelativas da chapa superior',
        is_top=False
    )

    # 3. Foot
    draw_foot_fabrication(f'{out}/fab_pezinho.pdf')

    print(f"\n✓ 3 PDFs de fabricação gerados em {out}/")
    print(f"  fab_chapa_superior.pdf — para cortador de chapas")
    print(f"  fab_chapa_inferior.pdf — para cortador de chapas")
    print(f"  fab_pezinho.pdf — para torneiro")
