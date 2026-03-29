"""Kleines Beispiel fuer eine Main Loop mit Menue."""


def menue_anzeigen() -> None:
    print("\n=== MINI TODO APP ===")
    print("1) Aufgabe anzeigen")
    print("2) Aufgabe hinzufuegen")
    print("3) Aufgabe loeschen")
    print("4) Beenden")


def main() -> None:
    aufgaben = ["Python wiederholen", "Uebung loesen"]

    while True:
        menue_anzeigen()
        wahl = input("Deine Wahl (1-4): ").strip()

        if wahl == "1":
            if not aufgaben:
                print("Keine Aufgaben vorhanden.")
            else:
                for i, aufgabe in enumerate(aufgaben, start=1):
                    print(f"{i}. {aufgabe}")

        elif wahl == "2":
            neu = input("Neue Aufgabe: ").strip()
            if neu:
                aufgaben.append(neu)
                print("Aufgabe gespeichert.")
            else:
                print("Leere Eingabe wurde ignoriert.")

        elif wahl == "3":
            if not aufgaben:
                print("Es gibt nichts zu loeschen.")
                continue

            for i, aufgabe in enumerate(aufgaben, start=1):
                print(f"{i}. {aufgabe}")

            eintrag = input("Welche Nummer loeschen? ").strip()
            if not eintrag.isdigit():
                print("Bitte eine gueltige Zahl eingeben.")
                continue

            index = int(eintrag) - 1
            if 0 <= index < len(aufgaben):
                geloescht = aufgaben.pop(index)
                print(f"Geloescht: {geloescht}")
            else:
                print("Nummer ausserhalb des Bereichs.")

        elif wahl == "4":
            print("Programm beendet. Bis bald.")
            break

        else:
            print("Ungueltige Eingabe. Bitte 1, 2, 3 oder 4 waehlen.")

# Dieser Block startet das Programm nur dann,
# wenn die Datei direkt ausgefuehrt wird.
# Bei einem Import in eine andere Datei wird main() nicht automatisch gestartet.
if __name__ == "__main__":
    main()
