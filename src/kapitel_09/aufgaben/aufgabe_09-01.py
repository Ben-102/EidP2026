# Aufgabe 09-01
#  TODO: Ihre Lösung hier
eintraege = []
eintraege = input("Hinzufügen: ")

with open("logbuch.txt", "a") as logbuch:
    for i in eintraege:
        logbuch.write(i)
