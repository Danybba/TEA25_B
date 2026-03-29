"""Kleines Numpy-Beispiel: Noten analysieren."""

try:
    import numpy as np
except ImportError:
    print("Numpy ist nicht installiert. Installiere es mit: pip install numpy")
    raise SystemExit

noten = np.array([1.3, 2.0, 2.7, 1.7, 2.3, 1.0, 3.0, 2.0])

print("Noten:", noten)
print("Durchschnitt:", round(np.mean(noten), 2))
print("Median:", round(np.median(noten), 2))
print("Beste Note:", np.min(noten))
print("Schlechteste Note:", np.max(noten))

# Bonus: Wie viele Noten sind 2.0 oder besser?
gut = np.sum(noten <= 2.0)
print("Anzahl <= 2.0:", int(gut))
