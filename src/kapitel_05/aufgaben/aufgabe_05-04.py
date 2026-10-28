# Aufgabe 05-04
#  TODO: Ihre Lösung hier
netto_preise = [99.99, 14.50, 42.00, 120.55]
brutto_preise = []

print(f"Netto-Preise: {netto_preise}")

for i in netto_preise:
    brutto_preise.append(int(i) * 0.19)

print(brutto_preise)
