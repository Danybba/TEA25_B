"""Sehr kleines Beispiel: Datei schreiben und lesen."""

DATEINAME = "notiz.txt"

# 1) Schreiben (uerschreibt Datei)
with open(DATEINAME, "w", encoding="utf-8") as datei:
    datei.write("Hallo Kurs!\n")
    datei.write("Heute lernen wir Datei-I/O in Python.\n")

# 2) Anhaengen (fuegt unten an)
with open(DATEINAME, "a", encoding="utf-8") as datei:
    datei.write("Das ist eine dritte Zeile.\n")

# 3) Lesen
with open(DATEINAME, "r", encoding="utf-8") as datei:
    inhalt = datei.read()

print("Dateiinhalt:\n")
print(inhalt)
