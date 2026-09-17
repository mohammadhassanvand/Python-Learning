"""
Spinning Donut
--------------
The classic terminal donut, ported to readable Python.
Renders a rotating 3D torus as ASCII characters using nothing but
trigonometry, a z-buffer, and a light-direction dot product.

Run it in a real terminal (not an IDE's built-in console) for the
smoothest animation:

    python3 donut.py

Press Ctrl+C to stop.
"""

import math
import os
import time

R1, R2 = 1, 2          # tube radius, torus radius
K2 = 5                  # distance of the torus from the viewer
WIDTH, HEIGHT = 80, 44  # terminal character grid
K1 = WIDTH * K2 * 3 / (8 * (R1 + R2))  # projection scale

LUMINANCE_RAMP = ".,-~:;=!*#$@"


def render_frame(A: float, B: float) -> str:
    cosA, sinA = math.cos(A), math.sin(A)
    cosB, sinB = math.cos(B), math.sin(B)

    output = [" "] * (WIDTH * HEIGHT)
    zbuffer = [0.0] * (WIDTH * HEIGHT)

    theta = 0.0
    while theta < 2 * math.pi:
        costheta, sintheta = math.cos(theta), math.sin(theta)

        phi = 0.0
        while phi < 2 * math.pi:
            cosphi, sinphi = math.cos(phi), math.sin(phi)

            circlex = R2 + R1 * costheta
            circley = R1 * sintheta

            x = circlex * (cosB * cosphi + sinA * sinB * sinphi) - circley * cosA * sinB
            y = circlex * (sinB * cosphi - sinA * cosB * sinphi) + circley * cosA * cosB
            z = K2 + cosA * circlex * sinphi + circley * sinA
            ooz = 1 / z

            xp = int(WIDTH / 2 + K1 * ooz * x)
            yp = int(HEIGHT / 2 - K1 * ooz * y * 0.5)

            luminance = (
                cosphi * costheta * sinB
                - cosA * costheta * sinphi
                - sinA * sintheta
                + cosB * (cosA * sintheta - costheta * sinA * sinphi)
            )

            if luminance > 0 and 0 <= xp < WIDTH and 0 <= yp < HEIGHT:
                idx = xp + yp * WIDTH
                if ooz > zbuffer[idx]:
                    zbuffer[idx] = ooz
                    lum_index = int(luminance * 8)
                    output[idx] = LUMINANCE_RAMP[min(lum_index, len(LUMINANCE_RAMP) - 1)]

            phi += 0.02
        theta += 0.07

    rows = [
        "".join(output[row * WIDTH:(row + 1) * WIDTH])
        for row in range(HEIGHT)
    ]
    return "\n".join(rows)


def main():
    A, B = 0.0, 0.0
    clear = "\x1b[H\x1b[2J"  # move cursor home + clear screen
    try:
        while True:
            print(clear + render_frame(A, B))
            A += 0.05
            B += 0.03
            time.sleep(1 / 30)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
