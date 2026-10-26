# Aufgabe 04-03
#  TODO: Ihre Lösung hier

einkaufsliste = []

while True:
    artikel = input(
        "Gib einen Artikel für die Einkaufsliste ein (oder 'fertig' zum Beenden):"
    )
    if artikel == "fertig":
        break
    einkaufsliste.append(artikel)

print("--- Deine Einkaufsliste ---" + einkaufsliste)
