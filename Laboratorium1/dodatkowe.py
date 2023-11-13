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
