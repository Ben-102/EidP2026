# Aufgabe 06-05
#  TODO: Ihre Lösung hier
rollen_rechte = {
    "admin": {"lesen", "schreiben", "löschen", "benutzer_verwalten"},
    "editor": {"lesen", "schreiben"},
    "gast": {"lesen"},
}
rollen = []
for i in rollen_rechte:
    rollen.append(i)


print(f"Verfügbare Rollen: {', '.join(rollen)}")
rolle_eingabe = input("Gib deine Rolle ein:")
berechtigung = input("Welche Berechtigung wird benötigt?")

if berechtigung in rollen_rechte[rolle_eingabe]:
    print("f")

print(f"Zugriff gewährt: Ein {rolle_eingabe} darf")
