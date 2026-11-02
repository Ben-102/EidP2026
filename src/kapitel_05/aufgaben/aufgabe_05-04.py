# Aufgabe 05-04
#  TODO: Ihre Lösung hier
netto_preise = [99.99, 14.50, 42.00, 120.55]
brutto_preise = []

print(f"Netto-Preise: {netto_preise}")

for i in netto_preise:
    brutto_preise.append(round(i * 1.19, 2))

print(f"Brutto-Preise (ink. 19% MwSt.): {brutto_preise}")
