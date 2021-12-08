tabela = [10, 2, 3, 11, "xyz", 5, 7, 4, 14, "abc", 16, 6, 20, 13, "qwerty"]

evenNum =[]
oddNum = []
error = []

for i in tabela:
    if not isinstance(i, int) and not isinstance(i, float):
        error.append(i)
    elif i % 2 == 0:
        evenNum.append(i)
    else:
        oddNum.append(i)

max_even = evenNum[0]
for x in evenNum:
    if max_even < x:
        max_even = x

min_odd = oddNum[0]
for y in oddNum:
    if min_odd > y:
        min_odd = y

print("Maksymalny elemant parzysty to: ", str(max_even))
print("Minimany elemant nieparzysty to: ", str(min_odd))
print("Błędne dane", str(error))