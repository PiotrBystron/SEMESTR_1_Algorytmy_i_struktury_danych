def minimum_petla_for(tablica):

    minimum = tablica[0]
    ile = 1

    for x in tablica:
        ile += 1
        if x < minimum:
            minimum = x
    return minimum, ile

tablica = [90, 80, 10, 20, 4, 45, 99, 3, 10, 100]

print("Minimalny element i ilość porównań", minimum_petla_for(tablica))