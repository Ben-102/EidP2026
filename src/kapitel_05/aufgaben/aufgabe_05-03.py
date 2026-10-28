# Aufgabe 05-03
#  TODO: Ihre Lösung hier
lagerbestand = [("Laptop", 15), ("Maus", 35), ("Tastatur", 8), ("Bildschirm", 5)]
print(f"Kritischer Lagerbestand (unter 10 Stück):")
for i in lagerbestand:
    if i[1] < 10:
        print("")
