def potega(a, n):

    if n == 0:
        return 1
    elif n < 0:
        return 1 / potega(a, -n)
    else:
        return a * potega(a, n - 1)


wynik = potega(5, 3)
print(f"a^n to {wynik}")
