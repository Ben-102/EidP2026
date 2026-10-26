# Aufgabe 04-04
#  TODO: Ihre Lösung hier
summe = 0
liste = [10, -5, 20, 0, -15, 8]
print(f"Gegebene Liste: {liste}")
for i in liste:
    if i >= 0:
        summe = summe + i
    else:
        print(f"Ignorierte negative Zahl: {i}")
print(f"Die Summe der positiven Zahlen ist: {summe}")
