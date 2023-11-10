import random
# Zad 3

dlugosc = int(input("Podaj długość prostokąta "))
szerokosc = int(input("Podaj szerokość prostokąta "))
obwod_prostokata = 2*dlugosc+2*szerokosc
print("Obwód prostokąta wynosi ", obwod_prostokata)
pole_prostokata = dlugosc*szerokosc
print("Pole prostokąta wynosi ", pole_prostokata)

# Zad 4

cena_paliwa = 6.5
droga = float(input("Ile przejechałeś kilometrów? "))
spalanie = float(input("Jakie jest spalanie Twojego samochodu? "))
zuzycie_paliwa = droga*spalanie/100
print("Zużycie wynosi ", zuzycie_paliwa)
koszty_podrozy = cena_paliwa*zuzycie_paliwa
print("Koszty podróży wyniosą ", koszty_podrozy, "zł")

# Zad 4.1


cena_paliwa = 6.5
droga = random.randint(1, 100000)
spalanie = float(input("Jakie jest spalanie Twojego samochodu? "))
zuzycie_paliwa = droga*spalanie/100
print("Zużycie wynosi ", zuzycie_paliwa)
koszty_podrozy = cena_paliwa*zuzycie_paliwa
print("Koszty podróży wyniosą ", koszty_podrozy, "zł")


# Zad 5

dlugosc = int(input("Podaj długość prostokąta "))
szerokosc = int(input("Podaj szerokość prostokąta "))
obwod_prostokata = 2*dlugosc+2*szerokosc
print("Obwód prostokąta wynosi ", obwod_prostokata)
pole_prostokata = dlugosc*szerokosc
print(f"Pole prostokąta wynosi {dlugosc*szerokosc}")

cena_paliwa = 6.5
droga = float(input("Ile przejechałeś kilometrów ?"))
spalanie = float(input("Jakie jest spalanie Twojego samochodu? "))
zuzycie_paliwa = droga*spalanie/100
print(f"Zużycie wynosi {droga*spalanie/100}")
koszty_podrozy = cena_paliwa*zuzycie_paliwa
print("Koszty podróży wyniosą ", koszty_podrozy, "zł")
