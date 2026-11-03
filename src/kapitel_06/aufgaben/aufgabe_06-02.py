# Aufgabe 06-02
#  TODO: Ihre Lösung hier
Satz = "Python ist super! Ja, wirklich super."
Satz = Satz.lower()
Satz = Satz.replace("!", "")
Satz = Satz.replace(".", "")
Satz = Satz.replace(",", "")
satzdictionary = Satz.split()

haeufigkeit = {}

for i in satzdictionary:
    haeufigkeit[i] = haeufigkeit.get(i, 0) + 1

print("Häufigkeit der Wörter:")
for i in haeufigkeit:
    print(f"- {i}: {haeufigkeit[i]}")
