# Aufgabe 03-04
#  TODO: Ihre Lösung hier
zahl1 = float(input("Gib die erste Zahl ein: "))
zahl2 = float(input("Gib die zweite Zahl ein: "))
operation = input("Gib die Operation ein (+, -, *, /): ")

if operation == "+":
    print(f"Das Ergebnis von {zahl1} + {zahl2} ist: {zahl1 + zahl2}")
elif operation == "-":
    print(f"Das Ergebnis von {zahl1} - {zahl2} ist: {zahl1 - zahl2}")
elif operation == "*":
    print(f"Das Ergebnis von {zahl1} * {zahl2} ist: {zahl1 * zahl2}")
else:
    print(f"Das Ergebnis von {zahl1} / {zahl2} ist: {zahl1 / zahl2}")
