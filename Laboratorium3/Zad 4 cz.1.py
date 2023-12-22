# a)
imie = input("Podaj imię ")
print(f"Witaj {imie}")

# b)
wiek = int(input("Podaj swój wiek "))
print(f"Twój wiek to {wiek}")

# c)
imie1 = input("Podaj imię ")
nazwisko = input("Podaj nazwisko ")
print(imie1[0], nazwisko[0])

# d)
zdanie = input("Napisz jakieś zdanie: ")
print((zdanie + " ") * 5)

# e)
zdanie1 = input("Podaj pierwsze zdanie ")
zdanie2 = input("Podaj drugie zdanie ")

print(zdanie1 + " " + zdanie2)

#  f) połączenie łańcuchów z podpunktu e)
polowa_pierwszego = len(zdanie1)//2
polowa_drugiego = len(zdanie2)//2

polaczone_zdanie = zdanie1[:polowa_pierwszego] + zdanie2[polowa_drugiego:]

print(polaczone_zdanie)
