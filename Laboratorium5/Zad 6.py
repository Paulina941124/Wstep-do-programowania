import math
import keyword
funkcje_w_math = [nazwa for nazwa in dir(math) if callable(getattr(math, nazwa))]

print(f"Funkcje w module math: {funkcje_w_math}")

funkcje_w_math = tuple(nazwa for nazwa in dir(math) if callable(getattr(math, nazwa)))

print(f"Funkcje w module math: {funkcje_w_math}")


slowa_kluczowe = keyword.kwlist
print(f"Słowa kluczowe w Pythonie: {slowa_kluczowe}")
