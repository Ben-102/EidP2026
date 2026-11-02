# Aufgabe 05-05
#  TODO: Ihre Lösung hier
adressen = [
    "test@example.com",
    "user.name@domain.co",
    "user@localhost",
    "no-at-sign.com",
    "user@.com",
    "@domain.com",
]
gadressen = []

for i in adressen:
    if i.count("@") == 1 and i.find(".") > i.find("@"):
        gadressen.append(i)


print(f"Ursprüngliche Liste: {adressen}\nGültige Email-Adressen: {gadressen}")
