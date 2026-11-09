# Aufgabe 07-03
#  TODO: Ihre Lösung hier
def noten_statistik(*noten: float):
    ergebnis = {}
    ergebnis["beste"] = min(noten)
    ergebnis["schlechteste"] = max(noten)
    ergebnis["durchschnitt"] = sum(noten) / len(noten)
    return ergebnis


print(f"Statistik 1: {noten_statistik(1.0, 1.3, 2.0, 4.0, 2.7, 2.5)}")
print(f"Statistik 1: {noten_statistik(2.3)}")
print(f"Statistik 1: {noten_statistik()}")
