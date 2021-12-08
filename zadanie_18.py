def minimum_petla_for(t_odd):
    minimum = t_odd[0]
    for x in t_odd:
        if x < minimum:
            minimum = x
    return minimum

def maximum_petla_for(t_even):
    maximum = t_even[0]
    for y in t_even:
        if y > maximum:
            maximum = y
    return maximum

tablica = [42,38,44,14,10,17,16,82,73]

t_even = tablica[0::2]
t_odd = tablica[1::2]

print("Dane ", tablica)
print()
print("Nieparzyste indeksy tablicy", t_odd)
print("Parzyste indeksy tablicy", t_even)
print()
print("Minimalny element wśród nieparzystych indeksów tablicy", minimum_petla_for(t_odd))
print("Maksymalny element wśród parzystych indeksów tablicy", maximum_petla_for(t_even))