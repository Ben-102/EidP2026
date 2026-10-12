import random

zufallszahl = random.randint(1, 10)
zahl = int(
    input("""--- Zahlenratespiel ---\n
Ich habe mir eine Zahl zwischen 1 und 10 ausgedacht. Rate mal!\nDein Tipp: """)
)
versuche = 0
while zahl != zufallszahl:
    if zufallszahl < zahl:
        print("Zu hoch! Versuche es nochmal.")
    elif zufallszahl > zahl:
        print("Zu niedrig! Versuche es nochmal.")
    zahl = int(input("Dein Tipp: "))
    versuche = versuche + 1
print(f"Korrekt! Du hast die Zahl {zufallszahl} in {versuche} Versuchen erraten!")
