# Aufgabe 05-01
#  TODO: Ihre Lösung hier
noten = [88, 92, 77, 95, 81]
noten.sort()

print(
    f"Ursprüngliche Noten: {noten}\nSchlechtestes Ergebnis {noten[0]} entfernt.\nNote 94 hinzugefügt."
)
noten[0] = 94
noten.sort()
print(f"Finale Notenliste: {noten}\nNeuer Durchschnitt: {sum(noten) / sum(noten)}")
