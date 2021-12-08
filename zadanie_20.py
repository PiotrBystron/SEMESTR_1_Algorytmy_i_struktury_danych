tablica = [10, 2, 3, 11, 5, 7, 4, 14, 16, 6, 20, 13]

minimum = tablica[0] 
maximum = tablica[0] 

for i in tablica:
    
    for y in tablica:
        if y > maximum:
            maximum = y

    for x in tablica:
        if x < minimum:
            minimum = x

print("Minimalny element tablicy to: ", minimum)
print("Maksymalny element tablicy to: ", maximum)