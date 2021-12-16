# Selection Sort
# Idee: In jedem Durchlauf
#       Minimum an den  Anfang

liste = [5, 7, 4, 9, 8, 1, 3, 0]
#        0  1  2  3  4  5  6  7  Index

# Ausgabe der unsortierten Liste
print(liste)

# merke wird benutzt, um sich die Position des kleinsten Elements der unsortierten Liste zu merken
merke = 0

# äußere Schleife: wird so oft durchgeführt, wie die Liste Elemente hat (hier achtmal)
# links: kennzeichnet beginn der unsortierten Liste
for links in range(0, len(liste)):
    
    # merke zunächst auf den Beginn der unsortierten Liste gesetzt
    merke = links
    
    # innere Schleife: Vergleich der Nachbarelemente
    # kleineres wird gemerkt
    for k in range(links, len(liste)):
        
        # wenn das Elemente an k kleiner ist als das gemerkte...
        if liste[k] < liste[merke]:
            
            # dann merke dir k
            merke = k
    
    # tausche das kleinste Element mit dem an links
    liste[merke], liste[links] = liste[links], liste[merke]
    
    # Ausgabe des aktuellen Schleifendurchlaufs nach Tausch
    print(liste)