import random
import string

listy = []
x = int(input("Podaj max liczbe liter: "))
n = int(input("Podaj liczbę elementow: "))

for _ in range(n):
    dlugosc_ciagu = random.randint(1, x)
    litera = "".join(random.choice(string.ascii_lowercase) for _ in range(dlugosc_ciagu))
    listy.append(litera)
print(listy)

# a) wypisanie elementow
z = sum(len(znaki) for znaki in listy)
print(f"Ilość znaków listy to: {z}")

# b) ilosc liter k
k ="k"
suma_k = sum(element.count(k) for element in listy if k in element)
print(f"Ilość wystąpień litery k to {suma_k}")

# c wystapienia kt
kt = "kt"
suma_kt = sum(element.count(kt) for element in listy if kt in element)
print(f"Ilość wystąpień kt to: {suma_kt}")

# d dluzsze niz s

s = int(input("Podaj długość ciągu "))

liczba_zn_el = [element for element in listy if len(element) > s]

if liczba_zn_el:
    print(f"Ciągi dłuższe od s to {liczba_zn_el}")
else:
    print("Nie ma dłuższych ciągów od s")

# e dodanie liter a i z

a = "a"
y = "z"

nowy = [a + element + y for element in listy]

print(nowy)
