# Selection Sort
# Idee: In jedem Durchlauf
#       Minimum an den Anfang

liste = [5, 7, 4, 9, 8, 1, 3, 0]
#        0  1  2  3  4  5  6  7  Index
merke = 0

for links in range(len(liste)):
    merke = links

    for i in range(links, len(liste)):
        if liste[i] < liste[merke]:
            merke = i
    liste[links], liste[merke] = liste[merke], liste[links]

print(liste)