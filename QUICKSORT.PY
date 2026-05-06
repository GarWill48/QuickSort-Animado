"""
Visualizador de Quicksort con Matplotlib
=========================================
Muestra paso a paso:
  - Pivote destacado (naranja)
  - Elementos comparándose (azul)
  - Intercambios (amarillo)
  - Elementos ya ordenados (verde)
  - Subarreglo activo delimitado con líneas punteadas
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.animation import FuncAnimation
import random

# ── Paleta de colores ──────────────────────────────────────────────────────────
COLOR_DEFAULT  = "#1e3a5f"   # sin procesar
COLOR_PIVOT    = "#ff6b35"   # pivote
COLOR_COMPARE  = "#3b82f6"   # comparando
COLOR_SWAP     = "#f59e0b"   # intercambiando
COLOR_SORTED   = "#00c97a"   # ordenado (posición final)
COLOR_ACTIVE   = "#2d5a8e"   # subarreglo activo
BG_COLOR       = "#070d1a"
TEXT_COLOR      = "#e2e8f0"

# ── Generador de pasos de Quicksort ───────────────────────────────────────────
def quicksort_steps(arr):
    """Genera cada estado del algoritmo como un dict."""
    a = arr[:]
    n = len(a)
    sorted_indices = set()
    steps = []

    def partition(lo, hi):
        pivot_val = a[hi]
        steps.append({
            "arr": a[:], "pivot": hi,
            "comparing": [], "swapped": [],
            "sorted": sorted_indices.copy(),
            "range": (lo, hi),
            "phase": "pivot",
            "msg": f"Pivote elegido: {pivot_val}  (índice {hi})"
        })
        i = lo - 1
        for j in range(lo, hi):
            steps.append({
                "arr": a[:], "pivot": hi,
                "comparing": [i + 1, j], "swapped": [],
                "sorted": sorted_indices.copy(),
                "range": (lo, hi),
                "phase": "compare",
                "msg": f"Comparando a[{j}]={a[j]}  vs  pivote={pivot_val}"
            })
            if a[j] <= pivot_val:
                i += 1
                a[i], a[j] = a[j], a[i]
                steps.append({
                    "arr": a[:], "pivot": hi,
                    "comparing": [], "swapped": [i, j],
                    "sorted": sorted_indices.copy(),
                    "range": (lo, hi),
                    "phase": "swap",
                    "msg": f"Intercambio: a[{i}]↔a[{j}]"
                })
        a[i + 1], a[hi] = a[hi], a[i + 1]
        pi = i + 1
        sorted_indices.add(pi)
        steps.append({
            "arr": a[:], "pivot": pi,
            "comparing": [], "swapped": [],
            "sorted": sorted_indices.copy(),
            "range": (lo, hi),
            "phase": "placed",
            "msg": f"✓ Pivote {a[pi]} en posición final: índice {pi}"
        })
        return pi

    def qs(lo, hi):
        if lo >= hi:
            if lo == hi:
                sorted_indices.add(lo)
            return
        steps.append({
            "arr": a[:], "pivot": -1,
            "comparing": [], "swapped": [],
            "sorted": sorted_indices.copy(),
            "range": (lo, hi),
            "phase": "subarray",
            "msg": f"Procesando subarreglo [{lo} … {hi}]"
        })
        pi = partition(lo, hi)
        qs(lo, pi - 1)
        qs(pi + 1, hi)

    qs(0, n - 1)
    for k in range(n):
        sorted_indices.add(k)
    steps.append({
        "arr": a[:], "pivot": -1,
        "comparing": [], "swapped": [],
        "sorted": sorted_indices.copy(),
        "range": (0, n - 1),
        "phase": "done",
        "msg": f"¡Ordenamiento completado en {len(steps)} pasos!"
    })
    return steps


# ── Configuración inicial ──────────────────────────────────────────────────────
N = 20
data = random.sample(range(5, 100), N)
steps = quicksort_steps(data)
total = len(steps)

fig, ax = plt.subplots(figsize=(13, 6))
fig.patch.set_facecolor(BG_COLOR)
ax.set_facecolor(BG_COLOR)

bars = ax.bar(range(N), data, color=COLOR_DEFAULT,
              edgecolor="#0a1628", linewidth=0.8)

# Líneas de partición (punteadas)
line_lo = ax.axvline(x=-1, color="#ffffff33", linestyle="--", linewidth=1.2)
line_hi = ax.axvline(x=-1, color="#ffffff33", linestyle="--", linewidth=1.2)

# Etiqueta del pivote
pivot_text = ax.text(0, 0, "", fontsize=9, color=COLOR_PIVOT,
                     ha="center", va="bottom",
                     fontweight="bold",
                     bbox=dict(boxstyle="round,pad=0.2", fc="#ff6b3522", ec=COLOR_PIVOT, lw=1))

# Título principal
title = ax.set_title("QUICKSORT — Visualizador",
                     color=TEXT_COLOR, fontsize=15, fontweight="bold", pad=14)

# Subtítulo (fase actual)
subtitle = fig.text(0.5, 0.01, "", ha="center", fontsize=10,
                    color="#94a3b8", style="italic")

# Contador de pasos
step_counter = fig.text(0.01, 0.97, "", ha="left", fontsize=9, color="#475569")

# Barra de progreso (usando axhline en un eje auxiliar)
prog_ax = fig.add_axes([0.1, 0.94, 0.8, 0.012])
prog_ax.set_facecolor("#1e293b")
prog_ax.set_xlim(0, total)
prog_ax.set_ylim(0, 1)
prog_ax.axis("off")
prog_bar = prog_ax.barh(0.5, 0, height=1, color=COLOR_PIVOT, left=0)

# Leyenda
legend_items = [
    mpatches.Patch(color=COLOR_PIVOT,   label="Pivote"),
    mpatches.Patch(color=COLOR_COMPARE, label="Comparando"),
    mpatches.Patch(color=COLOR_SWAP,    label="Intercambiando"),
    mpatches.Patch(color=COLOR_SORTED,  label="Ordenado"),
    mpatches.Patch(color=COLOR_ACTIVE,  label="Subarreglo activo"),
]
ax.legend(handles=legend_items, loc="upper left",
          facecolor="#0d1829", edgecolor="#1e3a5f",
          labelcolor=TEXT_COLOR, fontsize=8, framealpha=0.9)

ax.set_xlim(-0.8, N - 0.2)
ax.set_ylim(0, 105)
ax.tick_params(colors=TEXT_COLOR, labelsize=8)
ax.spines[:].set_color("#1e293b")
ax.yaxis.label.set_color(TEXT_COLOR)

# Índices bajo las barras
for i in range(N):
    ax.text(i, -4, str(i), ha="center", va="top",
            fontsize=7, color="#334155")


# ── Función de actualización ───────────────────────────────────────────────────
def update(frame_idx):
    s = steps[frame_idx]
    arr      = s["arr"]
    pivot    = s["pivot"]
    cmp      = s["comparing"]
    swp      = s["swapped"]
    srt      = s["sorted"]
    lo, hi   = s["range"]
    phase    = s["phase"]

    for i, bar in enumerate(bars):
        bar.set_height(arr[i])
        if i in srt:
            bar.set_color(COLOR_SORTED)
        elif i == pivot:
            bar.set_color(COLOR_PIVOT)
        elif i in swp:
            bar.set_color(COLOR_SWAP)
        elif i in cmp:
            bar.set_color(COLOR_COMPARE)
        elif lo <= i <= hi:
            bar.set_color(COLOR_ACTIVE)
        else:
            bar.set_color(COLOR_DEFAULT)

    # Líneas de subarreglo
    line_lo.set_xdata([lo - 0.5, lo - 0.5])
    line_hi.set_xdata([hi + 0.5, hi + 0.5])
    line_lo.set_visible(phase not in ("done",))
    line_hi.set_visible(phase not in ("done",))

    # Etiqueta del pivote
    if pivot >= 0 and phase in ("pivot", "compare", "swap"):
        pivot_text.set_position((pivot, arr[pivot] + 2))
        pivot_text.set_text(f"P={arr[pivot]}")
        pivot_text.set_visible(True)
    else:
        pivot_text.set_visible(False)

    # Subtítulo
    subtitle.set_text(s["msg"])
    color_map = {
        "pivot": COLOR_PIVOT, "compare": COLOR_COMPARE,
        "swap": COLOR_SWAP, "placed": COLOR_SORTED,
        "subarray": "#60a5fa", "done": COLOR_SORTED,
    }
    subtitle.set_color(color_map.get(phase, TEXT_COLOR))

    # Contador
    step_counter.set_text(f"Paso {frame_idx + 1} / {total}")

    # Barra de progreso
    prog_bar[0].set_width(frame_idx + 1)

    return bars


# ── Animación ─────────────────────────────────────────────────────────────────
ani = FuncAnimation(
    fig, update,
    frames=total,
    interval=300,    # ms entre frames (ajustable)
    repeat=False,
    blit=False
)

plt.tight_layout(rect=[0, 0.05, 1, 0.93])
plt.show()