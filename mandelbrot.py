"""
Mandelbrot Zoom
---------------
Renders a continuous zoom into the Mandelbrot set at "Seahorse Valley",
a coordinate famous for showing intricate detail at almost any depth.

Each frame is saved as a PNG in ./frames/. String them together with
ffmpeg to get the zoom video:

    ffmpeg -framerate 30 -i frames/frame_%04d.png -pix_fmt yuv420p out.mp4

Requires: pip install numpy pillow
"""

import math
import os

import numpy as np
from PIL import Image

WIDTH, HEIGHT = 800, 800
CX, CY = -0.7436438870, 0.1318259042   # Seahorse Valley
ZOOM_FACTOR = 0.97                      # scale *= this, every frame
N_FRAMES = 200
OUT_DIR = "frames"


def mandelbrot(cx: float, cy: float, scale: float, max_iter: int):
    """Return a (H, W) array of smoothed escape-time values."""
    x = np.linspace(-1, 1, WIDTH) * scale + cx
    y = np.linspace(-1, 1, HEIGHT) * scale + cy
    C = x[None, :] + 1j * y[:, None]

    Z = np.zeros_like(C)
    div_time = np.full(C.shape, max_iter, dtype=float)
    mask = np.ones(C.shape, dtype=bool)

    for n in range(max_iter):
        Z[mask] = Z[mask] * Z[mask] + C[mask]
        escaped = mask & (np.abs(Z) > 2)
        # smooth coloring: fractional escape count avoids banding
        with np.errstate(divide="ignore", invalid="ignore"):
            div_time[escaped] = n + 1 - np.log(np.log(np.abs(Z[escaped]))) / math.log(2)
        mask &= ~escaped
        if not mask.any():
            break

    div_time[mask] = max_iter  # points that never escaped -> black
    return div_time, mask


def palette(div_time, mask, max_iter, phase=0.0):
    """Map escape time to a cyclic RGB color; interior points are black."""
    t = (div_time / max_iter * 3.0 + phase) % 1.0
    sat, val = 0.75, 1.0

    h6 = t * 6.0
    i = np.floor(h6).astype(int) % 6
    f = h6 - np.floor(h6)
    p = val * (1 - sat)
    q = val * (1 - sat * f)
    u = val * (1 - sat * (1 - f))

    conds = [i == k for k in range(6)]
    r = np.select(conds, [val, q, p, p, u, val])
    g = np.select(conds, [u, val, val, q, p, p])
    b = np.select(conds, [p, p, u, val, val, q])

    r = np.where(mask, 0.0, r)
    g = np.where(mask, 0.0, g)
    b = np.where(mask, 0.0, b)

    rgb = (np.stack([r, g, b], axis=-1) * 255).astype(np.uint8)
    return rgb


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    scale = 1.5
    max_iter = 150

    for frame in range(N_FRAMES):
        div_time, mask = mandelbrot(CX, CY, scale, max_iter)
        rgb = palette(div_time, mask, max_iter, phase=frame / N_FRAMES * 0.6)
        Image.fromarray(rgb, "RGB").save(f"{OUT_DIR}/frame_{frame:04d}.png")

        print(f"frame {frame+1}/{N_FRAMES}  scale={scale:.2e}  max_iter={max_iter}")
        scale *= ZOOM_FACTOR
        max_iter += 2  # zoom deeper -> need more iterations to resolve detail


if __name__ == "__main__":
    main()
