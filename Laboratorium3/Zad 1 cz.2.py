import random
import string


def losowy_zbior(dl_min, dl_max):
    dlugosc = random.randint(dl_min, dl_max)
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(dlugosc))


n = int(input("Podaj ilość elementów: "))
mini = 1
maxi = int(input("podaj maksymalną ilość znaków elementu: "))
lista = [losowy_zbior(mini, maxi) for _ in range(n)]
print("Losowa lista ciągów: ", lista)

# Zamiana listy na krotkę

krotka = tuple(lista)
print("Krotka: ", krotka)
# a)

ilosc_znakow = sum(len(znaki) for znaki in krotka)
print(f"Ilość znaków w krotce: {ilosc_znakow}")

# b)
szukana = "k"
ilosc_k = sum(znak.count(szukana) for znak in krotka)
print(f"Ilość liter k w krotce:{ilosc_k}")

# c)
szukana2 = "kt"
ilosc_kt = sum(fragment.count(szukana2) for fragment in krotka)
print(f"Ilość kt w krotce to {ilosc_kt}")

# d)
s = int(input("Podaj ilość elementów szukanych ciągów: "))
wieksze_od_s = [ciag for ciag in krotka if len(ciag) > s]
krotka2 = tuple(wieksze_od_s)
print(f"Ciągi dłuższe od s: {krotka2}")
