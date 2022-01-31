

def mendikamentenmenge(n, dosis):
    n = n - 1
    if n > 0:
        return mendikamentenmenge(n, dosis * 0.6) 
    else:
        return dosis
dosis = mendikamentenmenge(5, 5)
print(dosis)