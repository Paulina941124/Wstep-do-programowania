# Zad2

x = int(input("Podaj ilość gwiazdek "))

for i in range(0, x):
    linia = "* " * x
    print(linia)

# Zad3

podstawa = int(input("Podaj ilość * w podstawie choinki "))

for i in range(1, podstawa + 1):
    liczba_znakow = podstawa - i
    odstep = " " * liczba_znakow
    wiersz1 = odstep + "* "*i
    print(wiersz1)
