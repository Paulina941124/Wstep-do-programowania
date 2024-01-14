# a)
def imie_wiek(imie, wiek):
    """
    Jest to funkcja,która wypisuje dwa parametry
    param1: imię
    param2:wiek
    """

    print(imie_wiek.__doc__)
    print("Imię:", imie)
    print("Wiek:", wiek)


imie = input("Podaj imię: ")
wiek = int(input("Podaj wiek: "))

imie_wiek(imie, wiek)

# b) z domyślnym wiekiem

wiek = 20
imie_wiek(imie, wiek)
