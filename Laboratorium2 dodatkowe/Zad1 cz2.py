import math
# z uzyciem continue

while True:
    a = input("Podaj daną nr 1.")
    if a.isdigit():
        print("To jest liczba.")
        continue
    else:
        print("To nie jest nieujemna liczba całkowita.")
        break
# bez użycia continue
while True:
    b = input("Podaj daną nr 2: ")

    if b.isdigit():
        print("To  jest liczba.")
    else:
        print("To nie jest nieujemna liczba całkowita")
        break

# licząca pierwiastek
while True:
    c = input("Podaj daną nr 3.")
    if c.isdigit():
        liczba = int(c)
        pierw = math.sqrt(liczba)
        print(f"Pierwiastek z tej liczby to {pierw}.")
        continue
    else:
        print("Dziękujemy za skorzystanie z naszej aplikacji.")
        break
