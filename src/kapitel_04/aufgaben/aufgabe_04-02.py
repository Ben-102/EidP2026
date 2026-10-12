# Aufgabe 04-02
#  TODO: Ihre Lösung hier
zahl = 1

while zahl < 101:
    if zahl % 3 == 0:
        print("Fizz")
    elif zahl % 5 == 0:
        print("Buzz")
    else:
        print(zahl)
    zahl = zahl + 1
