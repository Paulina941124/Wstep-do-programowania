# Zad 1
# a)
x1 = int(input("Podaj dowolny argument dla funkcji a(x) "))
if x1 > 0:
    a1 = 2*x1
    print("Dla tego argumentu funkcja przyjmuje wartość ", a1)
elif x1 == 0:
    print("Dla argumentu 0 funkcja przyjmuje wartość 0.")
elif x1 < 0:
    a2 = -3*x1
    print("Dla tego argumentu funkcja przyjmuje wartość ", a2)

# b)
x2 = int(input("Podaj dowolny argument dla funkcji b(x)"))
if x2 >= 1:
    b1 = x2**2
    print(f"Wartość funkcji dla tego argumentu to {b1}")
elif x2 < 1:
    print(f"Dla tego argumentu funkcja przyjmuje wartość {x2}")

# c)
x3 = int(input("Podaj argument dla funkcji c(x) "))
if x3 > 2:
    c1 = 2+x3
    print(f"Wartość funkcji dla tego argumentu to {c1}.")
elif x3 == 2:
    print("Wartość funkcji dla argumetu 2 to 8.")
elif x3 < 2:
    c2 = x3-4
    print(f"Wartość funkcji dla tego argumentu to {c2}.")

# Zad 2

# Pytania
a = str(input("Czy pada deszcz? (tak/nie) "))
b = str(input("Czy jest autobus na przystanku? "))

if a == "tak" and b == "tak":
    print("Weź parasol. Dostaniesz się na uczelnię.")
elif a == "tak" and not b == "tak":
    print("Nie dostaniesz się na uczelnię.")
elif not a == "tak" and b == "tak":
    print("Dostaniesz się na uczelnię. Miłego dnia i pięknej pogody")
