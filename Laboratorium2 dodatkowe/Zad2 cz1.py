n = int(input("Podaj liczbe studentów: "))

suma = 0

s = 1
while True:
    punkty = float(input(f"Podaj liczbę punktów dla studenta {s}: "))

    if punkty < 0 or punkty > 100:
        print("Wartość punktów nie mieści się w przedziale 1-100.")
        continue

    suma += punkty
    s += 1

    if s > n:
        break

srednia = suma / n
print(f"Średnia liczba punktów w grupie: {srednia}")
