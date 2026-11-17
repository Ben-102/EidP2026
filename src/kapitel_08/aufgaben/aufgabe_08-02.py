# Aufgabe 08-02
#  TODO: Ihre Lösung hier
class BankKonto:
    def __init__(self, inhaber, kontostand):
        self.inhaber = inhaber
        self.kontostand = kontostand

    def __str__(self):
        return f"Neues Konto für Max Mustermann mit {self.kontostand} EUR eröffnet."

    def einzahlen(self, betrag):
        self.kontostand += betrag
        print(f"Kontostand nach Einzahlung: {self.kontostand} EUR")

    def abheben(self, betrag):
        if self.kontostand >= betrag:
            self.kontostand -= betrag
            return f"Abhebung erfolgreich. Neuer Kontostand: {self.kontostand} EUR"
        else:
            return "Warnung: Abhebung nicht möglich. Kontostand zu gering."


k1 = BankKonto("Ben", 1000)
print(k1)
print(k1.einzahlen(200))
print(k1.abheben(2000))
print(k1.abheben(1000))
