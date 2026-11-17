# Aufgabe 08-03
#  TODO: Ihre Lösung hier
class Mitarbeiter:
    def __init__(self, name, gehalt):
        self.name = name
        self._gehalt = gehalt

    @property
    def gehalt(self):
        return f"Anna hat ein Gehalt von {self._gehalt} EUR."

    @gehalt.setter
    def gehalt(self, neues_gehalt):
        if neues_gehalt >= 0:
            self._gehalt = neues_gehalt
            print(f"Gehalt erfolgreich auf {self._gehalt} EUR geändert.")
        else:
            print(
                "Fehler: Das Gehalt darf nicht negativ sein. Wert wurde nicht geändert."
            )


m1 = Mitarbeiter("Dieter", 11000)
print(m1.gehalt)
m1.gehalt = 13402
print(m1.gehalt)
