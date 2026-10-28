# Aufgabe 05-02
#  TODO: Ihre Lösung hier
verkaufszahlen = [12, 15, 13, 18, 19, 22, 21, 20, 23, 25, 24, 27]

sortedverkaufszahlen = sorted(verkaufszahlen)
staerkste = sortedverkaufszahlen[-3:]
print(f"Die drei umsatzstärksten Monate hatten Verkäufe von: {staerkste}")

for i in verkaufszahlen:
    start = 0 
    end = 3
    temp = verkaufszahlen[start:end]
    if temp > 