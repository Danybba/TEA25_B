"""Pygal Mini-Dashboard: Balken + Radar fuer Notenvergleich.

Erzeugt zwei SVG-Dateien:
- noten_balken.svg
- noten_radar.svg
"""

try:
    import pygal
except ImportError:
    print("Pygal fehlt. Installation: pip install pygal")
    raise SystemExit

namen = ["Anna", "Ben", "Cem", "Dina", "Elif"]
python_noten = [1.3, 2.0, 2.7, 1.7, 1.0]
mathe_noten = [2.0, 2.3, 2.0, 1.3, 1.7]

# 1) Balkendiagramm
bar = pygal.Bar(title="Notenvergleich: Python vs Mathe")
bar.x_labels = namen
bar.y_title = "Note (kleiner ist besser)"
bar.add("Python", python_noten)
bar.add("Mathe", mathe_noten)
bar.render_to_file("noten_balken.svg")

# 2) Radar-Diagramm fuer einen schnellen Gesamtvergleich
radar = pygal.Radar(title="Klassenprofil je Fach")
radar.x_labels = namen
radar.add("Python", python_noten)
radar.add("Mathe", mathe_noten)
radar.render_to_file("noten_radar.svg")

print("Fertig: noten_balken.svg und noten_radar.svg wurden erstellt.")
print("Tipp: SVG in VS Code oeffnen oder im Browser anzeigen.")
