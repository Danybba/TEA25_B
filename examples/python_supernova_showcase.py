"""Interaktive Python-Showcase-Demo: Terminal + Grafik.

Was ist daran "krass":
- Echtzeit-Physik mit Gravitation (mehrere Koerper)
- Interaktive Steuerung per Tastatur und Maus
- Live-Status im Terminal
- Reines Python ohne externe Pakete (nur tkinter)

Start:
    python examples/python_supernova_showcase.py
"""

from __future__ import annotations

import math
import random
import time
import tkinter as tk
from dataclasses import dataclass

BREITE = 1100
HOEHE = 700
HINTERGRUND = "#06070a"
G = 1600.0
DT = 0.016


@dataclass
class Body:
    name: str
    x: float
    y: float
    vx: float
    vy: float
    mass: float
    radius: float
    color: str
    trail: list[tuple[float, float]]


class SupernovaShowcase:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Python Supernova Showcase")

        self.canvas = tk.Canvas(self.root, width=BREITE, height=HOEHE, bg=HINTERGRUND, highlightthickness=0)
        self.canvas.pack()

        self.running = True
        self.show_trails = True
        self.last_frame_time = time.perf_counter()
        self.frame_counter = 0
        self.last_stats_time = time.perf_counter()

        self.bodies: list[Body] = []
        self.stars: list[tuple[float, float, int]] = []

        self._build_starfield()
        self._build_world()
        self._bind_inputs()

        print("\n=== PYTHON SUPERNOVA SHOWCASE ===")
        print("Steuerung:")
        print("- Linksklick: Komet an diese Position setzen")
        print("- Leertaste: Pause/Fortsetzen")
        print("- T: Trails ein/aus")
        print("- C: Trails loeschen")
        print("- R: Welt neu starten")
        print("- ESC: Beenden")

    def _build_starfield(self) -> None:
        self.stars.clear()
        for _ in range(300):
            x = random.randint(0, BREITE)
            y = random.randint(0, HOEHE)
            size = random.choice([1, 1, 1, 2])
            self.stars.append((x, y, size))

    def _build_world(self) -> None:
        self.bodies = [
            Body("Sonne", BREITE / 2, HOEHE / 2, 0.0, 0.0, 26000.0, 16, "#ffd166", []),
            Body("Astra", BREITE / 2 + 180, HOEHE / 2, 0.0, -190.0, 40.0, 7, "#00d4ff", []),
            Body("Vega", BREITE / 2 - 260, HOEHE / 2, 0.0, 150.0, 70.0, 9, "#ef476f", []),
            Body("Nova", BREITE / 2, HOEHE / 2 + 320, 160.0, 0.0, 25.0, 6, "#06d6a0", []),
        ]

    def _bind_inputs(self) -> None:
        self.root.bind("<Escape>", lambda _e: self.root.destroy())
        self.root.bind("<space>", self._toggle_running)
        self.root.bind("t", self._toggle_trails)
        self.root.bind("c", self._clear_trails)
        self.root.bind("r", self._reset_world)
        self.canvas.bind("<Button-1>", self._spawn_comet)

    def _toggle_running(self, _event: tk.Event) -> None:
        self.running = not self.running
        print("Simulation:", "laeuft" if self.running else "pausiert")

    def _toggle_trails(self, _event: tk.Event) -> None:
        self.show_trails = not self.show_trails
        print("Trails:", "an" if self.show_trails else "aus")

    def _clear_trails(self, _event: tk.Event) -> None:
        for b in self.bodies:
            b.trail.clear()
        print("Trails geloescht")

    def _reset_world(self, _event: tk.Event) -> None:
        self._build_world()
        print("Welt zurueckgesetzt")

    def _spawn_comet(self, event: tk.Event) -> None:
        cx, cy = BREITE / 2, HOEHE / 2
        dx = event.x - cx
        dy = event.y - cy
        dist = max(1.0, math.hypot(dx, dy))

        # Tangentiale Startgeschwindigkeit fuer eine sichtbare Kurve.
        speed = 230.0 + random.uniform(-25.0, 25.0)
        vx = -dy / dist * speed
        vy = dx / dist * speed

        self.bodies.append(
            Body(
                name=f"Komet-{random.randint(100, 999)}",
                x=float(event.x),
                y=float(event.y),
                vx=vx,
                vy=vy,
                mass=8.0,
                radius=4,
                color="#f8ffe5",
                trail=[],
            )
        )
        print(f"Komet erzeugt bei ({event.x}, {event.y})")

    def _physics_step(self, dt: float) -> None:
        n = len(self.bodies)
        ax = [0.0] * n
        ay = [0.0] * n

        for i in range(n):
            bi = self.bodies[i]
            for j in range(n):
                if i == j:
                    continue
                bj = self.bodies[j]
                dx = bj.x - bi.x
                dy = bj.y - bi.y
                r2 = dx * dx + dy * dy + 20.0
                r = math.sqrt(r2)
                f = G * bj.mass / r2
                ax[i] += f * dx / r
                ay[i] += f * dy / r

        for i, b in enumerate(self.bodies):
            b.vx += ax[i] * dt
            b.vy += ay[i] * dt
            b.x += b.vx * dt
            b.y += b.vy * dt

            if self.show_trails:
                b.trail.append((b.x, b.y))
                if len(b.trail) > 120:
                    b.trail.pop(0)

        # Bodies ausserhalb des Sichtfelds entfernen (ausser Sonne)
        self.bodies = [
            b
            for b in self.bodies
            if b.name == "Sonne" or (-200 <= b.x <= BREITE + 200 and -200 <= b.y <= HOEHE + 200)
        ]

    def _draw(self) -> None:
        self.canvas.delete("all")

        for x, y, size in self.stars:
            color = "#cad2ff" if size == 2 else "#8f9bb3"
            self.canvas.create_oval(x, y, x + size, y + size, fill=color, outline=color)

        for b in self.bodies:
            if self.show_trails and len(b.trail) > 1:
                flat = [coord for point in b.trail for coord in point]
                self.canvas.create_line(*flat, fill=b.color, width=1, smooth=True)

            self.canvas.create_oval(
                b.x - b.radius,
                b.y - b.radius,
                b.x + b.radius,
                b.y + b.radius,
                fill=b.color,
                outline="",
            )

        self.canvas.create_text(
            14,
            14,
            anchor="nw",
            fill="#d8e2ff",
            font=("Consolas", 11, "bold"),
            text=f"Bodies: {len(self.bodies)}   Trails: {'ON' if self.show_trails else 'OFF'}   Running: {'YES' if self.running else 'NO'}",
        )

    def _print_stats(self) -> None:
        now = time.perf_counter()
        elapsed = now - self.last_stats_time
        if elapsed < 1.0:
            return

        fps = self.frame_counter / elapsed
        self.frame_counter = 0
        self.last_stats_time = now

        print(f"FPS ~ {fps:5.1f} | Bodies: {len(self.bodies):2d}")

    def loop(self) -> None:
        now = time.perf_counter()
        dt = min(0.03, now - self.last_frame_time)
        self.last_frame_time = now

        if self.running:
            self._physics_step(max(dt, DT))

        self._draw()
        self.frame_counter += 1
        self._print_stats()

        self.root.after(16, self.loop)

    def run(self) -> None:
        self.loop()
        self.root.mainloop()


def main() -> None:
    app = SupernovaShowcase()
    app.run()


if __name__ == "__main__":
    main()
