# Aufgabe 06-02
#  TODO: Ihre Lösung hier
Satz = "Python ist super! Ja, wirklich super."
Satz = Satz.lower()
Satz = Satz.replace("!", "")
Satz = Satz.replace(".", "")
Satz = Satz.replace(",", "")
satzdictionary = Satz.split()
print(satzdictionary)
