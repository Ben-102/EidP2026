# Aufgabe 06-01
#  TODO: Ihre Lösung hier
artikel = {"artikel_nr": "1", "name": "Hammer", "preis": "49.99", "lagerbestand": "14"}

print(f"Ursprünglicher Preis: {artikel['preis']} Euro")
temp = round(float(artikel["preis"]) * 1.1)
artikel["preis"] = str(temp)
artikel["hersteller"] = "TechPrime"
print(f"Das aktualisierte Artikelprofil:\n{artikel}")
