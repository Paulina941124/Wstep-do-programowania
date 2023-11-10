# Zad 3

x = float(input("Podaj pierwszą liczbę "))
y = float(input("Podaj drugą liczbę "))

dzialanie = int(input("Wybierz numer operacji: 1)dodawanie 2)odejmowanie 3)mnożenie 4)dzielenie "))

dodawanie = x+y
odejmowanie = x-y
mnozenie = x*y
dzielenie = x/y

if dzialanie == 1:
    print(f"Wynik to {dodawanie}.")
elif dzialanie == 2:
    print(f"Wynik to {odejmowanie}.")
elif dzialanie == 3:
    print(f"Wynik to {mnozenie}.")
elif dzialanie == 4:
    print(f"Wynik to {dzielenie}.")
else:
    print("To nie jest numer żadnej operacji.")
