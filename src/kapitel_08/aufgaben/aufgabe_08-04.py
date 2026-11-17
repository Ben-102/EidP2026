# Aufgabe 08-04
#  TODO: Ihre Lösung hier
class Mitglied:
    def __init__(self, namen):
        self.namen = namen


class Team:
    def __init__(self, team_namen):
        self.team_namen = team_namen
        self.Mitglieder = []

    def add_mitglied(self, mitglied):
        self.Mitglieder.append(mitglied)

    def show_mitglieder(self):
        print(f"Team: {self.team_namen}\n----------------")
        for i in self.Mitglieder:
            print(f"- {i.namen}")


team_dev = Team
team_dev = Team("Die Entwickler")
team_dev.add_mitglied(Mitglied("Anna"))
team_dev.add_mitglied(Mitglied("Ben"))
team_dev.add_mitglied(Mitglied("Clara"))

team_dev.show_mitglieder()
