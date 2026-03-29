"""Mini-Game: Rechen-Quiz mit persistenter Highscore-Datei."""

from __future__ import annotations

import json
import random
from pathlib import Path

HIGHSCORE_DATEI = Path("quiz_highscore.json")


def lade_highscore() -> dict:
    if not HIGHSCORE_DATEI.exists():
        return {"name": "-", "punkte": 0}

    with HIGHSCORE_DATEI.open("r", encoding="utf-8") as f:
        return json.load(f)


def speichere_highscore(name: str, punkte: int) -> None:
    daten = {"name": name, "punkte": punkte}
    with HIGHSCORE_DATEI.open("w", encoding="utf-8") as f:
        json.dump(daten, f, ensure_ascii=False, indent=2)


def stelle_frage() -> bool:
    a = random.randint(2, 12)
    b = random.randint(2, 12)
    korrekt = a * b

    eingabe = input(f"Was ist {a} * {b}? ").strip()
    if not eingabe.isdigit():
        print(f"Keine Zahl. Richtig waere {korrekt}.")
        return False

    if int(eingabe) == korrekt:
        print("Richtig!")
        return True

    print(f"Leider falsch. Richtig waere {korrekt}.")
    return False


def main() -> None:
    high = lade_highscore()
    print("=== RECHEN QUIZ ===")
    print(f"Aktueller Highscore: {high['name']} mit {high['punkte']} Punkten")

    name = input("Dein Name: ").strip() or "Spieler"
    runden = 5
    punkte = 0

    for nr in range(1, runden + 1):
        print(f"\nFrage {nr}/{runden}")
        if stelle_frage():
            punkte += 1

    print(f"\n{name}, du hast {punkte} von {runden} Punkten erreicht.")

    if punkte > int(high.get("punkte", 0)):
        speichere_highscore(name, punkte)
        print("Neuer Highscore gespeichert!")
    else:
        print("Kein neuer Highscore, aber gute Runde.")


if __name__ == "__main__":
    main()
