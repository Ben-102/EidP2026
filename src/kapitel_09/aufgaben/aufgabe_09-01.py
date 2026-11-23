# Aufgabe 09-01
import datetime

#  TODO: Ihre Lösung hier
eintraege = []
fertig = False
while fertig == False:
    eintraege = input("Hinzufügen: ")
    if eintraege == fertig:
        fertig = True
    else:
        continue
else:
    break

with open("logbuch.txt", "a") as logbuch:
    for i in eintraege:
        logbuch.write(i)

with open("logbuch.txt", "r") as logbuch:
    print(logbuch.read())
