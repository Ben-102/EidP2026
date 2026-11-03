# Aufgabe 06-05
#  TODO: Ihre Lösung hier
rollen_rechte = {
    "admin": {"lesen", "schreiben", "löschen", "benutzer_verwalten"},
    "editor": {"lesen", "schreiben"},
    "gast": {"lesen"},
}

for i in rollen_rechte:
    rollen = i


print(f"Verfügbare Rollen: {rollen}")
