# Aufgabe 09-01
#  TODO: Ihre Lösung hier
eintraege = []

while input("Hf: ") == "fertig":
    eintraege = input("Hinzufügen: ")

with open("logbuch.txt", "a") as logbuch:
    for i in eintraege:
        logbuch.write(i)

with open("logbuch.txt", "r") as logbuch:
    print(logbuch.read())
