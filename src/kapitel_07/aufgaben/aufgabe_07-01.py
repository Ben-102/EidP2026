# Aufgabe 07-01
#  TODO: Ihre Lösung hier
def berechne(zahl1: float, zahl2: float, operator: str):
    zahl1 = float(input("Gib die erste Zahl ein: "))
    zahl2 = float(input("Gib die zweite Zahl ein: "))
    operator = input("Gib die Operation ein (+, -, *, /): ")
    ergebnis = 0

    if operator == "+":
        ergebnis = zahl1 + zahl2
    elif operator == "-":
        ergebnis = zahl1 - zahl2
    elif operator == "*":
        ergebnis = zahl1 * zahl2
    else:
        if zahl2 == 0:
            print("Fehler: Division durch 0 ist nicht definiert!")
        else:
            ergebnis = zahl1 / zahl2

    print(
        f"# Bei Aufruf von berechne({zahl1}, {zahl2}, {operator})\nErgebnis: {ergebnis}"
    )

ergebnis = berechne(2,2,*)

print(f"Ergebnis: {ergebnis}")