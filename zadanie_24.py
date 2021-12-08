i = int(input("Podaj liczbę naturalną: "))

licznik = 1   

while i > 1:
    licznik += 1 
    if i % 2 == 0:
        i = i/2
    else:
        i = (i*3+1) / 2

print("META!")
print(licznik, "przejść przez szarą ramkę") 
print("Liczba = ", i)