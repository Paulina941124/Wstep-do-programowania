zdanie = input("Podaj przykładowe zdanie ")

zdanie1 = zdanie[::2]

print(zdanie1)

# Zad3 (wykorzystuje zdanie z zad2)

slowa = []

for slowo in zdanie.split():
    if len(slowo) > 1:
        nowe_slowo = slowo[0].capitalize() + slowo[1:-1] + slowo[-1].upper()
    else:
        nowe_slowo = slowo.upper()
    slowa.append(nowe_slowo)

zmienione_zdanie = ' '.join(slowa)

print("Zdanie po zmianach:", zmienione_zdanie)
