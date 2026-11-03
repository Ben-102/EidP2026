# Aufgabe 06-04
#  TODO: Ihre Lösung hier
bestellungen = [
    (101, "K-001"),
    (102, "K-002"),
    (103, "K-001"),
    (104, "K-003"),
    (105, "K-002"),
]
bestellungen_set = {bestellungen[1] for bestellungen in bestellungen}
print(f"Anzahl der eindeutigen Kunden: {len(bestellungen_set)}")
