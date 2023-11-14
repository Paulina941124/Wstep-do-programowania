# Zad 3 dodatkowe
litera = str(input("Podaj dowolną (małą lub wielką) literę: "))

if litera.islower():
    a = litera.upper()
    print(a)
elif litera.isupper():
    b = litera.lower()
    print(b)
else:
    print("To nie jest litera.")
