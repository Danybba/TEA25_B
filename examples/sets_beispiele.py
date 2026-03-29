"""Sets in Python.

Ein Set ist eine ungeordnete Sammlung eindeutiger Werte.
Typische Einsaetze:
- Duplikate entfernen
- Gemeinsamkeiten und Unterschiede zwischen Gruppen finden
- Schnelle Pruefung, ob ein Wert enthalten ist
"""

print("=== SETS KURZ ERKLAERT ===")
print("Set = ungeordnet + keine Duplikate")
print("Wichtige Operationen: &, -, |")
print()

# 1) Duplikate entfernen
namen_liste = ["anna", "ben", "anna", "dina", "ben", "emil"]
einzigartig = set(namen_liste)
print("Ohne Duplikate:", einzigartig)

# 2) Schnittmenge: wer war in beiden Kursen?
kurs_a = {"anna", "ben", "cem", "dina"}
kurs_b = {"ben", "dina", "finn"}
beide = kurs_a & kurs_b
print("In beiden Kursen:", beide)

# 3) Differenz: nur in Kurs A
nur_a = kurs_a - kurs_b
print("Nur in Kurs A:", nur_a)

# 4) Vereinigungsmenge: alle Teilnehmenden
alle = kurs_a | kurs_b
print("Alle zusammen:", alle)
