# Aufgabe 07-05
#  TODO: Ihre Lösung hier
mitarbeiter = [
    {"name": "Anna", "abteilung": "IT", "jahre_im_unternehmen": 5},
    {"name": "Ben", "abteilung": "Marketing", "jahre_im_unternehmen": 2},
    {"name": "Clara", "abteilung": "IT", "jahre_im_unternehmen": 8},
    {"name": "David", "abteilung": "IT", "jahre_im_unternehmen": 2},
]


def filter_mitarbeiter(mitarbeiter_liste: list[dict], **kriterien):

    gefillterte_liste = mitarbeiter_liste

    for kriterium, wert in kriterien.items():
        gefillterte_liste = list(
            filter(lambda m: m.get(kriterium) == wert, gefillterte_liste)
        )
    return gefillterte_liste


print(filter_mitarbeiter(mitarbeiter, abteilung="IT", name="Clara"))
