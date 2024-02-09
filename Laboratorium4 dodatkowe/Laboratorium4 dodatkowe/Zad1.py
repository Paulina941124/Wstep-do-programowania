def plec(x):
    ostatnia_litera = x[-1]
    if ostatnia_litera == "a":
        return "Kobieta"
    else:
        return "Mężczyzna"


x = input("Podaj imię: ")
plec(x)

lista = ["Ania", "Bartek", "Zosia", "Tomek", "Krystian"]

slownik = {x: plec(x) for x in lista}

print(slownik)
