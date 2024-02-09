def male_czy_duze(zdanie):
    wynik = {"male": 0, "duze": 0, "reszta_znakow": 0}
    for znak in zdanie:
        if znak.islower():
            wynik["male"] += 1
        elif znak.isupper():
            wynik["duze"] += 1
        elif znak is not znak.isalpha():
            wynik["reszta_znakow"] += 1
    return wynik

zdanie =input("Podaj swoje zdanie:" )

print(male_czy_duze(zdanie))