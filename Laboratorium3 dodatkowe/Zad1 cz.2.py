import random
liczby_uzyt = input("Podaj 5 liczb oddzielonych przecinkiem:")
lista = list(map(int, liczby_uzyt.split(",")))
print(lista)

if len(lista) != 5:
    print("Podano niewłaściwa ilosc elementow")
else:
    krotka = tuple(lista)
    print(f"Utworzona krotka: {krotka}")
    x = random.choice(krotka)
    print(f"Wylosowany element to {x}")

    if x == max(krotka):
        print("To największy element krotki")
    elif x == min(krotka):
        print("To najmniejszy element krotki")
    else:
        print("Ten element nie jest ani najmniejszy, ani największy w krotce.")
