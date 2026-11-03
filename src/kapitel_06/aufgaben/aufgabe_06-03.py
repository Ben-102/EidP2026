# Aufgabe 06-03
#  TODO: Ihre Lösung hier
python_kurs = ["Anna", "Ben", "Clara", "David"]
db_kurs = ["Clara", "David", "Eva", "Frank"]
python_kurs_set = set(python_kurs)
db_kurs_set = set(db_kurs)
print(
    f"Studierende in beiden Kursen: {python_kurs_set.intersection(db_kurs_set)}\nStudierende nur im Python-Kurs: {python_kurs_set.difference(db_kurs_set)}"
)
