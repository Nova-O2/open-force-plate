"""
Force Plate MVP — Technical Drawing Generator v2
Nova O2 Sports Science

Cells at ~62° diagonal, matching Phase 2 half-plate diagonal.
Feet at plate corners, cables toward center.

All dimensions in mm.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.transforms import Affine2D
import numpy as np

# =============================================================================
# DIMENSIONS (all in mm)
# =============================================================================

TOP_W = 600   # 60 cm (x-axis)
TOP_H = 500   # 50 cm (y-axis)

# Cell dimensions (Decent DYX-301 500kg)
CELL_L = 76       # body length (cota D)
CELL_W = 32       # body width (cota W)
CELL_HOLE_SPACING = 25   # between fixing holes (cota C)
CELL_HOLE_DIA = 13       # Ø fixing holes
CELL_CABLE_OFFSET = 15   # cable exit from end (cota B)

# Derived: distances from foot end along body axis
HOLE1_FROM_FOOT = CELL_L - CELL_CABLE_OFFSET - CELL_HOLE_SPACING  # 36 mm
HOLE2_FROM_FOOT = HOLE1_FROM_FOOT + CELL_HOLE_SPACING              # 61 mm

# Placement
MARGIN = 40  # mm from plate edge to foot center

# Angle: calculated from Phase 2 half-plate diagonal (300×500mm with 40mm margin)
# Half-plate support polygon: dx=300-2*MARGIN=220, dy=500-2*MARGIN=420
HALF_DX = (TOP_W / 2) - 2 * MARGIN  # 220 mm
HALF_DY = TOP_H - 2 * MARGIN         # 420 mm
DIAG_ANGLE = np.degrees(np.arctan2(HALF_DY, HALF_DX))  # ~62.4°

# =============================================================================
# CELL POSITIONS (foot at corner, body toward opposite corner of HALF plate)
# Phase 1 cells already at Phase 2 final angle
# =============================================================================

cells = {}

# C1/C3 are on left half → point toward opposite corner of left half-plate
# C2/C4 are on right half → point toward opposite corner of right half-plate
corners = {
    'C1': {'foot': (MARGIN, TOP_H - MARGIN),           'angle_deg': -DIAG_ANGLE},      # top-left → bottom-right (left half)
    'C2': {'foot': (TOP_W - MARGIN, TOP_H - MARGIN),   'angle_deg': -(180 - DIAG_ANGLE)},  # top-right → bottom-left (right half)
    'C3': {'foot': (MARGIN, MARGIN),                     'angle_deg': DIAG_ANGLE},       # bottom-left → top-right (left half)
    'C4': {'foot': (TOP_W - MARGIN, MARGIN),             'angle_deg': (180 - DIAG_ANGLE)},   # bottom-right → top-left (right half)
}

for name, info in corners.items():
    fx, fy = info['foot']
    a = np.radians(info['angle_deg'])
    ca, sa = np.cos(a), np.sin(a)

    h1x = fx + HOLE1_FROM_FOOT * ca
    h1y = fy + HOLE1_FROM_FOOT * sa
    h2x = fx + HOLE2_FROM_FOOT * ca
    h2y = fy + HOLE2_FROM_FOOT * sa
    cable_x = fx + CELL_L * ca
    cable_y = fy + CELL_L * sa

    cells[name] = {
        'foot': (fx, fy),
        'hole1': (h1x, h1y),
        'hole2': (h2x, h2y),
        'cable': (cable_x, cable_y),
        'angle_deg': info['angle_deg'],
    }

# =============================================================================
# BOTTOM PLATE
# =============================================================================

all_hx = [cells[n][h][0] for n in cells for h in ['hole1', 'hole2']]
all_hy = [cells[n][h][1] for n in cells for h in ['hole1', 'hole2']]
BM = 20  # margin
BOT_X0 = min(all_hx) - BM
BOT_Y0 = min(all_hy) - BM
BOT_W = max(all_hx) - min(all_hx) + 2 * BM
BOT_H = max(all_hy) - min(all_hy) + 2 * BM

# Gasket: matches cell base (56×32mm), holes horizontal in drawing
GASKET_W = 56  # matches cell base length (cota I)
GASKET_H = 32  # matches cell base width (cota W)

# =============================================================================
# DRAWING
# =============================================================================

def dim_line(ax, p1, p2, offset, text, horiz=True, fs=7):
    if horiz:
        y = p1[1] + offset
        ax.annotate('', xy=(p1[0], y), xytext=(p2[0], y),
                    arrowprops=dict(arrowstyle='<->', color='#333', lw=0.7))
        ax.text((p1[0]+p2[0])/2, y+3, text, ha='center', va='bottom', fontsize=fs, color='#333')
        ax.plot([p1[0], p1[0]], [p1[1], y], color='#999', lw=0.3, ls='--')
        ax.plot([p2[0], p2[0]], [p2[1], y], color='#999', lw=0.3, ls='--')
    else:
        x = p1[0] + offset
        ax.annotate('', xy=(x, p1[1]), xytext=(x, p2[1]),
                    arrowprops=dict(arrowstyle='<->', color='#333', lw=0.7))
        ax.text(x+3, (p1[1]+p2[1])/2, text, ha='left', va='center', fontsize=fs, color='#333', rotation=90)
        ax.plot([p1[0], x], [p1[1], p1[1]], color='#999', lw=0.3, ls='--')
        ax.plot([p2[0], x], [p2[1], p2[1]], color='#999', lw=0.3, ls='--')


def draw_cell(ax, cell, name):
    fx, fy = cell['foot']
    angle = cell['angle_deg']

    # Cell body (rotated rectangle)
    # Origin at foot end, body extends in direction of angle
    body = patches.FancyBboxPatch(
        (0, -CELL_W/2), CELL_L, CELL_W,
        boxstyle="round,pad=1",
        linewidth=1, edgecolor='#2266AA', facecolor='#CCE0FF', alpha=0.7, zorder=3
    )
    t = Affine2D().rotate_deg(angle).translate(fx, fy) + ax.transData
    body.set_transform(t)
    ax.add_patch(body)

    # Holes
    for hkey in ['hole1', 'hole2']:
        hx, hy = cell[hkey]
        c = plt.Circle((hx, hy), CELL_HOLE_DIA/2, fill=False, ec='black', lw=1, zorder=5)
        ax.add_patch(c)
        ax.plot([hx-3, hx+3], [hy, hy], color='black', lw=0.4, zorder=5)
        ax.plot([hx, hx], [hy-3, hy+3], color='black', lw=0.4, zorder=5)

    # Foot
    fc = plt.Circle((fx, fy), 7, fc='#FF6644', ec='#CC3311', lw=1.5, zorder=6)
    ax.add_patch(fc)

    # Cable direction arrow
    cx, cy = cell['cable']
    mx = (fx + cx) / 2
    my = (fy + cy) / 2
    ax.annotate('', xy=(cx, cy), xytext=(mx, my),
                arrowprops=dict(arrowstyle='->', color='green', lw=1), zorder=4)

    # Label
    lx = (fx + cell['hole2'][0]) / 2
    ly = (fy + cell['hole2'][1]) / 2
    # offset label perpendicular to cell axis
    perp_angle = angle + 90
    lx += 20 * np.cos(np.radians(perp_angle))
    ly += 20 * np.sin(np.radians(perp_angle))
    ax.text(lx, ly, name, ha='center', fontsize=9, fontweight='bold', color='#2266AA', zorder=7)


def draw_top_plate(ax):
    ax.set_title('PLACA SUPERIOR — Alumínio 6061-T6, 6mm\n50×60 cm — Células a ~62° (ângulo Fase 2)',
                 fontsize=11, fontweight='bold', pad=15)

    # Plate
    plate = patches.Rectangle((0, 0), TOP_W, TOP_H, lw=2, ec='black', fc='#E8E8E8', zorder=1)
    ax.add_patch(plate)

    # Phase 2 cut line
    ax.plot([TOP_W/2, TOP_W/2], [-15, TOP_H+15], color='red', lw=1, ls='-.', zorder=2)
    ax.text(TOP_W/2, TOP_H+20, 'CORTE FASE 2', ha='center', fontsize=7, color='red')

    # Draw cells
    for name, cell in cells.items():
        draw_cell(ax, cell, name)

    # Bottom plate outline (dashed)
    bot = patches.Rectangle((BOT_X0, BOT_Y0), BOT_W, BOT_H, lw=1.5,
                             ec='#AA6622', fc='none', ls='--', zorder=2)
    ax.add_patch(bot)
    ax.text(TOP_W/2, BOT_Y0 - 15,
            f'PLACA INFERIOR (tracejada) — {BOT_W:.0f}×{BOT_H:.0f} mm, 3mm',
            ha='center', fontsize=7, color='#AA6622')

    # Diagonal reference lines (cell to opposite corner)
    ax.plot([MARGIN, TOP_W - MARGIN], [TOP_H - MARGIN, MARGIN],
            color='#AAAAAA', lw=0.5, ls=':', zorder=1)
    ax.plot([TOP_W - MARGIN, MARGIN], [TOP_H - MARGIN, MARGIN],
            color='#AAAAAA', lw=0.5, ls=':', zorder=1)

    # Dimensions
    dim_line(ax, (0, 0), (TOP_W, 0), -45, f'{TOP_W} mm', horiz=True)
    dim_line(ax, (0, 0), (0, TOP_H), -45, f'{TOP_H} mm', horiz=False)
    dim_line(ax, (0, TOP_H - MARGIN), (MARGIN, TOP_H - MARGIN), 30, f'{MARGIN}', horiz=True)
    dim_line(ax, (MARGIN, TOP_H), (MARGIN, TOP_H - MARGIN), 15, f'{MARGIN}', horiz=False)

    # Legend
    ax.plot([], [], 'o', color='#FF6644', ms=8, label='Pézinho (M12×1.75)')
    ax.plot([], [], 'o', color='white', mec='black', ms=8, label=f'Furo Ø{CELL_HOLE_DIA}mm')
    ax.plot([], [], color='#2266AA', lw=5, alpha=0.3, label='Célula DYX-301 (~62°)')
    ax.plot([], [], color='#AA6622', lw=1.5, ls='--', label='Placa inferior')
    ax.plot([], [], color='red', lw=1, ls='-.', label='Corte Fase 2')
    ax.plot([], [], color='green', lw=1, label='Saída cabo')
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.06), ncol=3, fontsize=7)

    ax.set_xlim(-65, TOP_W + 65)
    ax.set_ylim(-70, TOP_H + 40)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.15)
    ax.set_xlabel('mm')
    ax.set_ylabel('mm')


def draw_bottom_plate(ax):
    ax.set_title(f'PLACA INFERIOR — Alumínio 3mm\n{BOT_W:.0f}×{BOT_H:.0f} mm',
                 fontsize=11, fontweight='bold', pad=15)

    plate = patches.Rectangle((BOT_X0, BOT_Y0), BOT_W, BOT_H, lw=2,
                               ec='black', fc='#F5E6D0', zorder=1)
    ax.add_patch(plate)

    for name, cell in cells.items():
        for hk in ['hole1', 'hole2']:
            hx, hy = cell[hk]
            c = plt.Circle((hx, hy), CELL_HOLE_DIA/2, fill=False, ec='black', lw=1, zorder=4)
            ax.add_patch(c)
            ax.plot([hx-3, hx+3], [hy, hy], color='black', lw=0.4)
            ax.plot([hx, hx], [hy-3, hy+3], color='black', lw=0.4)

        mid_x = (cell['hole1'][0] + cell['hole2'][0]) / 2
        mid_y = (cell['hole1'][1] + cell['hole2'][1]) / 2
        ax.text(mid_x, mid_y + 18, name, ha='center', fontsize=8, fontweight='bold', color='#AA6622')

    dim_line(ax, (BOT_X0, BOT_Y0), (BOT_X0 + BOT_W, BOT_Y0), -30, f'{BOT_W:.0f} mm')
    dim_line(ax, (BOT_X0, BOT_Y0), (BOT_X0, BOT_Y0 + BOT_H), -30, f'{BOT_H:.0f} mm', horiz=False)

    ax.set_xlim(BOT_X0 - 50, BOT_X0 + BOT_W + 50)
    ax.set_ylim(BOT_Y0 - 50, BOT_Y0 + BOT_H + 50)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.15)
    ax.set_xlabel('mm')
    ax.set_ylabel('mm')


def draw_gasket(ax):
    ax.set_title(f'JUNTA SUPERIOR — Aço 2mm\n{GASKET_W}×{GASKET_H} mm (×4)',
                 fontsize=11, fontweight='bold', pad=15)

    g = patches.Rectangle((0, 0), GASKET_W, GASKET_H, lw=2, ec='black', fc='#D0D0D0', zorder=1)
    ax.add_patch(g)

    # Holes horizontal (rotation applied during assembly)
    cx = GASKET_W / 2
    cy = GASKET_H / 2
    for dx in [-CELL_HOLE_SPACING/2, CELL_HOLE_SPACING/2]:
        hx = cx + dx
        c = plt.Circle((hx, cy), CELL_HOLE_DIA/2, fill=False, ec='black', lw=1, zorder=4)
        ax.add_patch(c)
        ax.plot([hx-2, hx+2], [cy, cy], color='black', lw=0.4)
        ax.plot([hx, hx], [cy-2, cy+2], color='black', lw=0.4)

    dim_line(ax, (0, 0), (GASKET_W, 0), -12, f'{GASKET_W}', fs=8)
    dim_line(ax, (0, 0), (0, GASKET_H), -12, f'{GASKET_H}', horiz=False, fs=8)
    dim_line(ax, (cx - CELL_HOLE_SPACING/2, cy), (cx + CELL_HOLE_SPACING/2, cy),
             12, f'{CELL_HOLE_SPACING}', fs=8)

    ax.text(GASKET_W/2, -18, f'Furos: 2× Ø{CELL_HOLE_DIA}mm\nRotação aplicada na montagem (~62°)',
            ha='center', fontsize=7)

    ax.set_xlim(-20, GASKET_W + 20)
    ax.set_ylim(-25, GASKET_H + 20)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.15)


def draw_cross_section(ax):
    ax.set_title('SEÇÃO TRANSVERSAL — Montagem\n(fora de escala)', fontsize=11, fontweight='bold', pad=15)
    ax.axis('off')

    w = 120
    x0 = 40
    y = 210

    layers = [
        ('Parafuso M12 (cabeça chata)', 4, '#666', x0, w),
        ('Placa superior 6mm alumínio', 14, '#C0C0C0', x0, w),
        ('Junta 2mm aço (56×32)', 5, '#888', x0+20, w-40),
        ('Célula DYX-301 (32mm, a ~62°)', 44, '#CCE0FF', x0+15, w-30),
        ('Placa inferior 3mm alumínio', 7, '#D4B896', x0+10, w-20),
        ('Porca M12 + arruela', 6, '#666', x0+40, 25),
    ]

    for label, h, color, lx, lw in layers:
        r = patches.Rectangle((lx, y), lw, -h, lw=1, ec='black', fc=color, zorder=2)
        ax.add_patch(r)
        ax.text(lx + lw + 8, y - h/2, label, va='center', fontsize=7)
        y -= h + 3

    # Foot
    fy = y - 5
    ax.plot([x0+w/2-5, x0+w/2+5], [fy, fy-22], color='#CC3311', lw=3)
    ax.plot([x0+w/2-12, x0+w/2+12], [fy-22, fy-22], color='#CC3311', lw=3)
    ax.text(x0+w/2+18, fy-11, 'Pézinho\nM12×1.75', fontsize=7, va='center')

    ax.plot([x0-20, x0+w+20], [fy-22, fy-22], color='brown', lw=2)
    ax.text(x0+w+25, fy-22, 'Piso', fontsize=7, va='center')

    # Bolt line
    ax.plot([x0+50, x0+50], [215, y+10], color='#333', lw=1.5, zorder=1)

    ax.set_xlim(15, 270)
    ax.set_ylim(fy-40, 230)
    ax.set_aspect('equal')


# =============================================================================
# GENERATE
# =============================================================================

if __name__ == '__main__':
    print("=" * 60)
    print("FORCE PLATE MVP — Dimensões (células a 45°)")
    print("=" * 60)
    print(f"\nPlaca superior: {TOP_W}×{TOP_H} mm (6mm)")
    print(f"Placa inferior: {BOT_W:.0f}×{BOT_H:.0f} mm (3mm)")
    print(f"Juntas (×4): {GASKET_W}×{GASKET_H} mm (2mm aço)")
    print(f"Margem borda→pé: {MARGIN}mm")

    print(f"\nCoordenadas (origem: canto inferior esquerdo):")
    print(f"{'Célula':<6} {'Ponto':<8} {'X':>8} {'Y':>8}")
    print("-" * 35)
    for n in ['C1', 'C2', 'C3', 'C4']:
        c = cells[n]
        print(f"{n:<6} {'Pé':<8} {c['foot'][0]:>8.1f} {c['foot'][1]:>8.1f}")
        print(f"{'':6} {'Furo 1':<8} {c['hole1'][0]:>8.1f} {c['hole1'][1]:>8.1f}")
        print(f"{'':6} {'Furo 2':<8} {c['hole2'][0]:>8.1f} {c['hole2'][1]:>8.1f}")
        print(f"{'':6} {'Cabo':<8} {c['cable'][0]:>8.1f} {c['cable'][1]:>8.1f}")

    # Figure
    fig, axes = plt.subplots(2, 2, figsize=(16, 14))
    fig.suptitle('NOVA O2 FORCE PLATE MVP — Desenho Técnico v2\n'
                 'Células a ~62° (diagonal Fase 2) | Dimensões em mm | 2026-04-01',
                 fontsize=14, fontweight='bold', y=0.98)

    draw_top_plate(axes[0, 0])
    draw_bottom_plate(axes[0, 1])
    draw_gasket(axes[1, 0])
    draw_cross_section(axes[1, 1])

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig('/workspace/03-engineering/nova-o2/force-plate/cad/force_plate_technical_drawing.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.savefig('/workspace/03-engineering/nova-o2/force-plate/cad/force_plate_technical_drawing.pdf',
                bbox_inches='tight', facecolor='white')
    print(f"\nSalvo: cad/force_plate_technical_drawing.[png|pdf]")

    plt.close('all')
