# Aufgabe 09-01
#  TODO: Ihre Lösung hier
eintraege = []

while input("Hf: ") == "fertig":
    continue
else:
    eintraege = input

with open("logbuch.txt", "a") as logbuch:
    for i in eintraege:
        logbuch.write(i)

with open("logbuch.txt", "r") as logbuch:
    print(logbuch.read())
