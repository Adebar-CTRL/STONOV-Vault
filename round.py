weekone = float(input("Inzidenz der ersten Woche eingeben"))
r = float(input("Wachstumsrate eingeben"))

for i in range(52):
    if r >= 1:
        weekone = weekone * r
    else:
       weekone = weekone / r
    
    if weekone < 50:
        if weekone < 35:
            print("Woche", i + 1, ":", round(weekone, 2), "Grün")
        else:
            print("Woche", i + 1, ":", round(weekone, 2), "Gelb")
    else:
        print("Woche", i + 1, ":", round(weekone, 2), "Rot")
    
    