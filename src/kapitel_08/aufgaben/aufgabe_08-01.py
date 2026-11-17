# Aufgabe 08-01
#  TODO: Ihre Lösung hier
class Produkt:
    def __init__(self, artikel_nr, namen, preis):
        self.artikel_nr = artikel_nr
        self.namen = namen
        self.preis = preis

    def __str__(self):
        return f"Produkt {self.artikel_nr}: {self.namen} - {self.preis}"


p1 = Produkt("A-123", "Gaming-Maus", 79.99)
print(p1)
