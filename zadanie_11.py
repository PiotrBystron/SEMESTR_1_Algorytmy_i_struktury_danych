def minimum_petla_while(tablica):
  
    minimum = tablica[0]
    i = 1
    ile = 1

    while i < len(tablica): 
        ile += 1
        if tablica[i] < minimum:
            minimum = tablica[i]
        i += 1
    return minimum, ile
  
#tablica = [90, 80, 10, 20, 4, 45, 99, 3, 10, 100, 2]
tablica = [90, 80]
print("Minimalny element i ilość porównań", minimum_petla_while(tablica))