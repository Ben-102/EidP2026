# Aufgabe 03-01
#  TODO: Ihre Lösung hier
punktzahl = int(input("Bitte gib deine erreichte Punktzahl ein: "))

if punktzahl > 89:
    print(f"Deine Note: Sehr Gut ({punktzahl} Punkte)")
elif punktzahl > 79:
    print(f"Deine Note: Gut ({punktzahl} Punkte)")
elif punktzahl > 64:
    print(f"Deine Note: Befriedigend ({punktzahl} Punkte)")
elif punktzahl > 49:
    print(f"Deine Note: Ausreichend ({punktzahl} Punkte)")
else:
    print(f"Deine Note: Durchgefallen ({punktzahl} Punkte)")
