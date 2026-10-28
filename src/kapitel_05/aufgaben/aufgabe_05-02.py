# Aufgabe 05-02
#  TODO: Ihre Lösung hier
verkaufszahlen = [12, 15, 13, 18, 19, 22, 21, 20, 23, 25, 24, 27]

sortedverkaufszahlen = sorted(verkaufszahlen)
staerkste = sortedverkaufszahlen[-3:]
print(f"Die drei umsatzstärksten Monate hatten Verkäufe von: {staerkste}")

start = 0
end = 3
quartal = 1
for i in range(4):
    summe = sum(verkaufszahlen[start:end])
    temp2 = 0
    if summe > temp2:
        temp2 = summe
        ergebnis = quartal
    start = start + 3
    end = end + 3
    quartal = quartal + 1

print(f"Das beste Quartal war das {ergebnis}. Quartal.")
