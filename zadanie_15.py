def maximum_index_petla_for(tablica):
    
    maximum = tablica[0]
    index = 0
    ile = 1

    for x in range(len(tablica)):
        ile += 1
        if tablica[x] > maximum:
            index = x
            maximum = tablica[x]
    return index, ile

tablica = [100, 1, 45, 99, 3, 10, 100, 1, 2, 100, 1]

print("Najmniejszy indeks elementu maksymalnego i ilość porównań", maximum_index_petla_for(tablica))