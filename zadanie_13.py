def minimum_index_petla_for(tablica):
    
    minimum = tablica[0]
    index = 0
    ile = 1

    for x in range(len(tablica)):
        ile += 1
        if tablica[x] < minimum:
            index = x
            minimum = tablica[x]
    return index, ile

tablica = [90, 4, 1, 45, 99, 3, 10, 100, 1, 2, 1]

print("Najmniejszy indeks elementu minimalnego i ilość porównań", minimum_index_petla_for(tablica))