# Aufgabe 07-03
#  TODO: Ihre Lösung hier
def noten_statistik(*noten: float):
    ergebnis = {"beste": float, "schlechteste": float, "durchschnitt": float}
    snoten = 0
    snoten = sorted(noten)
    ergebnis["beste"] = snoten[0]
    ergebnis["schlechteste"] = snoten[-1]
    ergebnis["durchschnitt"] = sum(snoten) / len(snoten)


print(f"Statistik 1: {noten_statistik(1.0, 1.3, 2.0, 4.0, 2.7, 2.5)}")
