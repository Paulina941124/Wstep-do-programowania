import random


def silnia(n):
    if n == 1:
        return 1
    else:
        return n * silnia(n-1)


nx = random.randint(1, 1000)
print(f"Wygenerowana liczba naturalna to {nx}")

wynik = silnia(nx)
print(f"n!={wynik}")
