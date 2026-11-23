# Aufgabe 09-01
from datetime import datetime

#  TODO: Ihre Lösung hier
eintraege = []

while True:
    eintrag = input("Hinzufügen: ")

    if eintrag == "fertig":
        break

    eintraege.append(eintrag)


with open("logbuch.txt", "a") as logbuch:
    for i in eintraege:
        logbuch.write(f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} - {i}\n")

with open("logbuch.txt", "r") as logbuch:
    print(logbuch.read())
