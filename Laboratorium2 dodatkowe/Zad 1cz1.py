n = int(input("Podaj liczbe studentów: "))

suma = 0

s = 1
while s <= n:
    punkty = float(input(f"Podaj liczbę punktów dla studenta {s}: "))
    suma += punkty
    s += 1
srednia = suma / n
print(f"Średnia liczba punktów w grupie: {srednia}")
