# Zad1

a = int(input("Podaj wspólczynnik a "))
b = int(input("Podaj współczynnik b "))
wynik = -a/b
print(f"Wynik równania 0=ax+b to x={-a/b}")

# Zad2

a = 16
b = 8
c = 12
p = (a+b+c)/2
P = (p*(p-a)*(p-b)*(p-c))**0.5
print(f"Pole trójkąta o bokach {a, b, c} wynosi ", P)

# Zad3

x = float(input("Podaj pierwszą liczbę "))
y = float(input("Podaj drugą liczbę "))

print(f"Wynik dodawania to {x+y}")
print(f"Wynik odejmowania to {x-y}")
print(f"Wynik mnożenia to {x*y}")
print(f"Wynik dzielenia to {x/y}")
