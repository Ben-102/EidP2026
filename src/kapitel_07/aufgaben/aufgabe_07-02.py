# Aufgabe 07-02
#  TODO: Ihre Lösung hier


def erstelle_gruss(name: str, anrede: str = "Sehr geehrte/r ", titel: str = ""):
    ergebnis = ""
    ergebnis = ergebnis + anrede + name
    return ergebnis


print(erstelle_gruss("Max Mustermann"))
print(erstelle_gruss(""))
