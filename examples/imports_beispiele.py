"""Imports: Standardbibliothek + eigener Import."""

import random
from datetime import date
from statistics import mean

from import_werkzeuge import begruessung, quadrat

namen = ["Anna", "Ben", "Cem", "Dina"]
auswahl = random.choice(namen)

noten = [1.7, 2.3, 1.3, 2.0]

print(begruessung(auswahl))
print("Heute ist:", date.today())
print("Durchschnittsnote:", round(mean(noten), 2))
print("Quadrat von 7:", quadrat(7))
