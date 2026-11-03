# Aufgabe 07-02
#  TODO: Ihre Lösung hier


def erstelle_gruss(name: str, anrede: str = "Sehr geehrte/r ", titel: str = ""):
    ergebnis = ""
    if titel != "":
        ergebnis = ergebnis + anrede + name
    return ergebnis


print(erstelle_gruss("Max Mustermann"))
print(erstelle_gruss("Ada Lovelace", anrede="Hallo Frau", titel="Prof. Dr."))
