# Aufgabe 04-06

import random
import string

# Nützliche Zeichenketten aus dem string-Modul holen.
# Alternativ könnten wir sie auch selbst definieren: klein = "abc..."
KLEINBUCHSTABEN = string.ascii_lowercase
GROSSBUCHSTABEN = string.ascii_uppercase
ZAHLEN = string.digits
SONDERZEICHEN = string.punctuation

# Tipps:
print(SONDERZEICHEN)

# experimentiere hier mehrfach mit SHIFT+ENTER
print(random.choice(SONDERZEICHEN))

#  TODO: Deine Lösung hier:
pw = []
print("--- Passwort-Generator ---")
KB = int(input("Anzahl Kleinbuchstaben: "))
GB = int(input("Anzahl Großbuchstaben: "))
Z = int(input("Anzahl Zahlen: "))
SZ = int(input("Anzahl Sonderzeichen: "))

while True:
    if KB > 0:
        pw.append(random.choice(GROSSBUCHSTABEN))
        KB = KB - 1
    else:
        break

print(pw)
