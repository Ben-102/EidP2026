# Aufgabe 09-03
#  TODO: Ihre Lösung hier
import csv

tabelle  = ["kunden_nr,name,stadt
K001,Anna Schmidt,Berlin
K002,Ben Meier,München
K003,Clara Wolf,Hamburg"]

with open("kunden.csv", "w", newline="") as kunden:
    writer = csv.writer(kunden)

    writer
