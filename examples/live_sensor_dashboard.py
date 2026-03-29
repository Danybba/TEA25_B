"""Live-Dashboard mit simulierten Sensordaten und CSV-Logging.

Start:
    python live_sensor_dashboard.py
Stop:
    Strg+C
"""

from __future__ import annotations

import csv
import os
import random
import time
from datetime import datetime

LOG_DATEI = "sensor_log.csv"


def clamp(wert: float, minimum: float, maximum: float) -> float:
    return max(minimum, min(maximum, wert))


def ascii_balken(wert: float, minimum: float, maximum: float, breite: int = 30) -> str:
    normiert = (wert - minimum) / (maximum - minimum)
    normiert = clamp(normiert, 0.0, 1.0)
    fuellung = int(normiert * breite)
    return "#" * fuellung + "-" * (breite - fuellung)


def schreibe_header_wenn_noetig(datei: str) -> None:
    if os.path.exists(datei):
        return

    with open(datei, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["zeit", "temperatur", "luftfeuchte", "puls"])


def logge_werte(datei: str, temperatur: float, luftfeuchte: float, puls: int) -> None:
    mit_zeit = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(datei, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([mit_zeit, f"{temperatur:.1f}", f"{luftfeuchte:.1f}", puls])


def bildschirm_leeren() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def main() -> None:
    schreibe_header_wenn_noetig(LOG_DATEI)

    temperatur = 21.0
    luftfeuchte = 45.0
    puls = 72

    print("Live-Dashboard startet. Stoppen mit Strg+C...")
    time.sleep(1.2)

    try:
        while True:
            temperatur = clamp(temperatur + random.uniform(-0.4, 0.4), 16.0, 30.0)
            luftfeuchte = clamp(luftfeuchte + random.uniform(-1.2, 1.2), 20.0, 90.0)
            puls = int(clamp(puls + random.randint(-2, 2), 45, 140))

            logge_werte(LOG_DATEI, temperatur, luftfeuchte, puls)

            bildschirm_leeren()
            print("=== LIVE SENSOR DASHBOARD ===")
            print(f"Log-Datei: {LOG_DATEI}")
            print(datetime.now().strftime("Zeit: %H:%M:%S"))
            print()

            print(f"Temperatur:  {temperatur:4.1f} C  [{ascii_balken(temperatur, 16.0, 30.0)}]")
            print(f"Luftfeuchte: {luftfeuchte:4.1f} %  [{ascii_balken(luftfeuchte, 20.0, 90.0)}]")
            print(f"Puls:        {puls:4d} bpm [{ascii_balken(float(puls), 45.0, 140.0)}]")
            print()
            print("Tipp: Oeffne sensor_log.csv fuer Live-Daten im Tabellenformat.")

            time.sleep(1.0)

    except KeyboardInterrupt:
        print("\nDashboard gestoppt. Daten wurden gespeichert.")


if __name__ == "__main__":
    main()
