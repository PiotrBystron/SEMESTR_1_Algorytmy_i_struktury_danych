data = int(input("Podaj datę do sprawdzenia:"))

if data % 4 == 0 and (data % 100 != 0 or data % 400 == 0):
    print(data, "jest przestępny")
else:
    print(data, "nie jest przestępny")