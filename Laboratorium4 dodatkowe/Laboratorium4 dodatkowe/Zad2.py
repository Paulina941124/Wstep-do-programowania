def wyswietl_i_znajdz_max(*args):
    print("Wartości parametrów:")
    for parametr in args:
        print(parametr)

    if args:
        max_wartosc = max(args)
        print(f"Największa wartość: {max_wartosc}")
        return max_wartosc
    else:
        print("Brak parametrów. Nie można znaleźć maksymalnej wartości.")
        return None


wynik = wyswietl_i_znajdz_max(5, 8, 2, 10, 3)
print("Zwrócona maksymalna wartość:", wynik)
