a = int(input("Podaj współczynnik a "))
b = int(input("Podaj współczynnik b "))
c = int(input("Podaj współczynnik c "))

# Obliczenie delty
delta = (b**2)-(4*a*c)
print(f"Delta wynosi {delta}.")
pierw_delta = delta**0.5

# rozwiązania równania

if delta > 0:
    x1 = (-b+pierw_delta)/(2*a)
    x2 = (-b-pierw_delta)/(2*a)
    print(f"Rozwiązania równania to {x1} i {x2}.")
elif delta == 0:
    x0 = -b/2*a
    print(f"Równanie ma jedno miejsce zerowe {x0}.")
else:
    print("Równanie nie ma rozwiązania")
