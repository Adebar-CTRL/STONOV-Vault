# Sortierprogramm nach bubblesort
# Autoren: Max Kutzner, Lea Hauptmann

def bubble_sort(liste):
    # für alle unsortierten Elemente
    for i in range(len(liste) - 1):
        # "Bubble-Prozess" -> 2 benachbarte Elemente vergleichen und bei Bedarf tauschen


        # nach der Schleife sind alle Elemente mit einem Index kleiner als len(liste) - i sortiert
        for j in range(len(liste) - i - 1):

            min_index = j
            nachbar = min_index +1
             
            if liste[min_index] > liste[nachbar]:
                liste[min_index], liste[nachbar] = liste[nachbar], liste[min_index]
            min_index = min_index + 1
            nachbar = min_index + 1

        # für ein besseres Verständis geben wir die Liste nach jedem "Bubble-Prozess" aus
        print(liste)
    return liste

liste_sortiert = bubble_sort([2, 9, 3, 8, 1, 7, 5, 4, 6])
print(liste_sortiert)