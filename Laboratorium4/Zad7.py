def odwrocony_string(string):
    return string[::-1]

a = str(input("Podaj tekst do odwrócenia: "))
nowy_string = odwrocony_string(a)

print(nowy_string)
