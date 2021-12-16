#a = (4,9,3,1)

#print(sorted(a))

liste = [3,9,2,1]

print(liste)
merke = 0

for links in range(0, len(liste)):
    merke = links
    for k in range(links, len(liste)):
        if liste[k] < liste[merke]:
            merke = k
    liste[merke], liste[links] = liste[links], liste[merke]
