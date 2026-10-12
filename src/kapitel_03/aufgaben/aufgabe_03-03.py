# Aufgabe 03-03
#  TODO: Ihre Lösung hier
bestellwert = float(input("Bitte geben Sie den Bestellwert ein: "))
Mitglied = input("Sind Sie Premium-Mitglied (ja/nein)? ")

if Mitglied == "ja":
    print(f"""--- VERSANDKOSTEN-RECHNER ---\n
Bestellwert:     {bestellwert} Euro\n
Versandkosten:    0.00 Euro\n
--------------------------\n
Gesamtbetrag:    {bestellwert} Euro""")
elif bestellwert < 50:
    print(f"""--- VERSANDKOSTEN-RECHNER ---\n
Bestellwert:     {bestellwert} Euro\n
Versandkosten:    4.99 Euro\n
--------------------------\n
Gesamtbetrag:    {bestellwert + 4.99} Euro""")
else:
    print(f"""--- VERSANDKOSTEN-RECHNER ---\n
    Bestellwert:     {bestellwert} Euro\n
    Versandkosten:    0.00 Euro\n
    --------------------------\n
    Gesamtbetrag:    {bestellwert} Euro""")
