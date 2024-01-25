# Zad 1

import random
import math
import cmath
import keyword
import datetime

a = random.randint(1, 11)
print(f"Szczęśliwy numerek to {a}")

lata = [1994, 1998, 2001, 2002, 2003, 2004]
b = random.choice(lata)
print(f"Szczęśliwy rocznik to:{b}")

liczby = list(range(1, 50))
wylosowane = random.sample(liczby, 6)

print("Wylosowane liczby to;", sorted(wylosowane))


# Zad 2
print(math.sqrt(81))
print(math.pow(8, 10))

print(math.sqrt(2)+math.sqrt(3)+math.sqrt(6))
print(cmath.sqrt(-5))
print(math.pow(125, 1/3))

# Zad 3



#Zad 4

data_dzisiejsza = datetime.date.today()
print(f"Data dzisiejsza to {data_dzisiejsza}")
from datetime import date
data_ost_zaj = date(2023, 12, 10)
print(f"Data ostatnich zajęć to {data_ost_zaj}")
data_kolosa = date(2024, 2, 11)
print(f"Data kolokwium to {data_kolosa}")
czas_od_zajec = data_dzisiejsza - data_ost_zaj
print(f"Od ostatnich zajęć minęło: {czas_od_zajec}")
czas_do_kol = data_kolosa - data_dzisiejsza
print(f"Czas do kolokwium to {czas_do_kol}")

# Zad 5
c = "for"
d = "print"
e = "break"
f = "done"
g = "bad"
print(keyword.iskeyword(c))
