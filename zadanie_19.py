tablica = [10, 6, 20, 13, 23, 40, 15]

pierwszyNajwiekszy = 0
drugiNajwiekszy = 0
index_drugiNajwiekszy = 0
index_pierwszyNajwiekszy = 0
ile = 1

for i in range(len(tablica)):
    ile += 1
    if tablica[i] > pierwszyNajwiekszy:
        if pierwszyNajwiekszy > drugiNajwiekszy:
            drugiNajwiekszy = pierwszyNajwiekszy
        index_drugiNajwiekszy = index_pierwszyNajwiekszy
        pierwszyNajwiekszy = tablica[i]
        index_pierwszyNajwiekszy = i
    elif tablica[i] > drugiNajwiekszy:
        drugiNajwiekszy = tablica[i]
        index_drugiNajwiekszy = i

print("Pierwszy największy element", pierwszyNajwiekszy)
print("Indesk - pierwszy największy element", index_pierwszyNajwiekszy)
print()
print("Drugi największy element", drugiNajwiekszy)
print("Indesk - drugi największy element", index_drugiNajwiekszy)
print()
print("ilość porównań", ile)