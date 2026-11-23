# Aufgabe 09-02
#  TODO: Ihre Lösung hier
tabelle = {}
try:
    with open("config.ini", "r") as config:
        for zeile in config:
            schlüssel, wert = zeile.split("=")
            tabelle[schlüssel] = wert

        print(f"Konfiguration erfolgreich geladen: {config}")
except FileNotFoundError:
    print(
        "Fehler: Konfigurationsdatei 'config.ini' nicht gefunden. Standardwerte werden verwendet."
    )
