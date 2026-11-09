# Aufgabe 07-03
#  TODO: Ihre Lösung hier
def noten_statistik(*noten: float):
    sorted(noten)
    beste = noten[0]
    schlechteste = noten[-1]
    durchschnitt = sum(noten) / len(noten)
    ergebnis = {}


print(f"Statistik 1: {noten_statistik(1.0, 1.3, 2.0, 4.0, 2.7, 2.5)}")
