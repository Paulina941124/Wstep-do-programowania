# Zad 4

zdanie = input("Podaj zdanie: ")

nowe_zdanie = ""
for i in range(len(zdanie)):
    if zdanie != "" and zdanie.count(zdanie[i]) > 1:
        nowe_zdanie += "@"
    else:
        nowe_zdanie += zdanie[i]

print("Nowe zdanie:  ", nowe_zdanie)

# Zad 5 Używam zdania z zad 4

slowa = zdanie.split()

longest = max(slowa, key=len)

dlugosc = len(longest)

print(f"Najdłuższe słowo to {longest} z liczbą liter równą {dlugosc}")

# Zad 6

x = input("Podaj ciąg znaków: ")

x = x.lower()
slowo = x[::-1]

if x == slowo:
    print(f"{x} - tak")
else:
    print(f"{x} - nie")
