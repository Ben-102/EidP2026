# Aufgabe 09-01
import datetime

#  TODO: Ihre Lösung hier
eintraege = []

while True:
    eintrag = input("Hinzufügen: ")

    if eintrag == "fertig":
        break

    eintraege.append(eintrag)


with open("logbuch.txt", "a") as logbuch:
    for i in eintraege:
        logbuch.write(i)

with open("logbuch.txt", "r") as logbuch:
    print(logbuch.read())
