import random


def gra(a, b):
    szukana_liczba = random.randint(a, b)
    print(f"Zakres liczb to {a} - {b}")
    for proba in range(1, 4):
        while True:
            try:
                liczba_uzytkownika = int(input(f"Podejście nr {proba}. Podaj swoja losową liczbę: "))
                break
            except ValueError:
                print("Podaj poprawną liczbę.")
        if szukana_liczba == liczba_uzytkownika:
            print("Gratulacje! Udało się!")
            break
        elif szukana_liczba > liczba_uzytkownika:
            print("Podałeś za małą liczbę.")
        elif szukana_liczba < liczba_uzytkownika:
            print("Podałeś za dużą liczbę.")
    else:
        print("To koniec! Wyczerpałeś limit prób!")

# Zakres liczb


while True:
    try:
        a = int(input("Podaj liczbę będącą początkiem zakresu: "))
        b = int(input("Podaj koniec zakresu, pamiętając, że musi to być liczba wyższa o co najmniej 10 od początku zakresu:"))
        if a >= b or b - a < 10:
            print("Zakres nie spełnia wymienionych warunków.")
        else:
            break
    except ValueError:
        print("Podaj poprawne liczby")

# początek gry
gra(a, b)
