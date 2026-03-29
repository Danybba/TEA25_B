"""Krasser ohne Zusatzpakete: ASCII-Heatmap fuer Zufallsdaten."""

import random

# Dunkel -> hell
palette = " .:-=+*#%@"

breite = 40
hoehe = 15

print("ASCII Heatmap")
print("-" * breite)

for _ in range(hoehe):
    zeile = []
    for _ in range(breite):
        wert = random.random()  # 0.0 bis 1.0
        index = int(wert * (len(palette) - 1))
        zeile.append(palette[index])
    print("".join(zeile))

print("-" * breite)
print("Je heller das Zeichen, desto groesser der Zufallswert.")
