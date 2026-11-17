# Aufgabe 07-04
#  TODO: Ihre Lösung hier
produkte = [
    {"name": "Laptop", "preis_netto": 1199.00},
    {"name": "Maus", "preis_netto": 25.00},
    {"name": "Tastatur", "preis_netto": 79.50},
]

ergebnis = list(
    map(
        lambda produkt: {
            "name": produkt["name"],
            "preis_netto": produkt["preis_netto"],
            "preis_brutto": round(produkt["preis_netto"] * 1.19, 2),
        },
        produkte,
    )
)

print(ergebnis)
