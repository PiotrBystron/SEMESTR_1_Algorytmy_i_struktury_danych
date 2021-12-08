def maximum_index_petla_for(tablica):
    
    minimum = tablica[0]
    index = 0
    ile = 1

    for x in range(len(tablica)):
        ile += 1
        if tablica[x] <= minimum:
            index = x
            minimum = tablica[x]
    return index, ile

tablica = [45, 44, 33, 22, 11, 99, 100, 1, 2, 1, 1, 20]

print("Indeks największego elementu i ilość porównań", maximum_index_petla_for(tablica))