dlugosc = float(input("Podaj długość w metrach do przeliczenia:"))
print()

cale = dlugosc/0.0254
stopy = dlugosc/0.0254/12
jardy = dlugosc/0.0254/12/3
mile = dlugosc/0.0254/12/3/1760

print(dlugosc,"m to:")
print(cale, "cali")
print(stopy, "stóp")
print(jardy, "jardów")
print(mile, "mili")