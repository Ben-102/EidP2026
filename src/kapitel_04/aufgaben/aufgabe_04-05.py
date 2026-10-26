# Aufgabe 04-05
#  TODO: Ihre Lösung hier

liste1 = ["     +++++     "]
liste2 = ["+++++++++++++++"]


ergebnis = []

for i in range(14):
    if i <= 4:
        ergebnis.append(liste1[0])
    elif i <= 9:
        ergebnis.append(liste2[0])
    else:
        ergebnis.append(liste1[0])

print("\n".join(ergebnis))
