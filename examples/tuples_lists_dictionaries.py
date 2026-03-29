"""Mini-Lernskript: Tuple vs Liste vs Dictionary.

Dieses Skript ist absichtlich sehr kleinschrittig aufgebaut,
damit du es live mit Studierenden durchgehen kannst.
"""

print("=== 1) Grundidee ===")
print("Tuple: feste Reihenfolge, unveraenderbar")
print("Liste: feste Reihenfolge, veraenderbar")
print("Dictionary: Schluessel -> Wert")


print("\n=== 2) Erstellen ===")
tup = ("rot", "gruen", "blau")
lst = ["rot", "gruen", "blau"]
dct = {"farbe1": "rot", "farbe2": "gruen", "farbe3": "blau"}

print("Tuple:", tup)
print("Liste:", lst)
print("Dictionary:", dct)


print("\n=== 3) Zugriff ===")
print("Tuple[0]:", tup[0])
print("Liste[0]:", lst[0])
print("Dictionary['farbe1']:", dct["farbe1"])


print("\n=== 4) Veraenderbarkeit ===")
print("Liste kann geaendert werden:")
lst[1] = "gelb"
print(lst)

print("Tuple kann NICHT geaendert werden:")
try:
	tup[1] = "gelb"
except TypeError as err:
	print("Fehler:", err)


print("\n=== 5) Laenge ===")
print("len(Tuple):", len(tup))
print("len(Liste):", len(lst))
print("len(Dictionary):", len(dct), "(Anzahl Schluessel)")


print("\n=== 6) Hinzufuegen ===")
print("Zur Liste hinzufuegen mit append:")
lst.append("lila")
print(lst)

print("Zum Dictionary hinzufuegen mit neuem Schluessel:")
dct["farbe4"] = "lila"
print(dct)

print("Beim Tuple nur indirekt (neu bauen):")
tup = tup + ("lila",)
print(tup)


print("\n=== 7) Iteration ===")
print("Tuple/Liste: direkt ueber Werte")
for wert in tup:
	print("Tuple-Wert:", wert)

for wert in lst:
	print("Listen-Wert:", wert)

print("Dictionary: ueber Schluessel und Werte")
for schluessel, wert in dct.items():
	print(schluessel, "->", wert)


print("\n=== 8) Wann nehme ich was? ===")
print("Tuple: feste Daten (z. B. Koordinaten)")
print("Liste: Sammlung, die sich aendern soll")
print("Dictionary: Daten mit Namen/Attributen")


print("\n=== 9) Mini-Beispiel aus der Praxis ===")
koordinate = (10, 20)  # Tuple: feste x/y Position
einkauf = ["Brot", "Milch"]  # Liste: kann wachsen
student = {"name": "Anna", "alter": 21}  # Dictionary: Attribute

einkauf.append("Eier")
student["kurs"] = "Python"

print("Koordinate:", koordinate)
print("Einkauf:", einkauf)
print("Student:", student)
