# Aufgabe 09-02
#  TODO: Ihre Lösung hier


with open("config.ini", "r") as name:
    if name.read != "":
        print(f"Konfiguration erfolgreich geladen: {name.read}")
    else:
        print(
            "Fehler: Konfigurationsdatei 'config.ini' nicht gefunden. Standardwerte werden verwendet. Konfiguration geladen: "
        )
