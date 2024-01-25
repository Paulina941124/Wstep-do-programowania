import random

def srednia_geo(krotka):
    iloczyn = 1
    for element in krotka:
        iloczyn *= element
    return iloczyn ** (1/len(krotka))


while True:
    try:
        zakres_poczatek = int(input("Podaj początek zakresu: "))
        zakres_koniec = int(input("Podaj koniec zakresu: "))
        if zakres_poczatek >= zakres_koniec:
            print("Początek zakresu musi być mniejszy niż koniec. Spróbuj ponownie.")
        else:
            break
    except ValueError:
        print("Podaj poprawne liczby")

krotka_elementow = tuple(random.randint(zakres_poczatek, zakres_koniec) for _ in range(10))


print(f"Krotka wygenerowanych elementów: {krotka_elementow}")


srednia_geo = srednia_geo(krotka_elementow)
print(f"Średnia geometryczna: {srednia_geo:.2f}")

