# Zad1

wiek = int(input("Podaj swój wiek w latach "))
if wiek < 4:
    print("Wstęp darmowy.")
elif wiek > 18:
    print("Bilet kosztuje 20zł.")
else:
    print("Bilet kosztuje 10 zł.")

# Zad2

litera = input("Podaj literę ")
if litera.isupper():
    print("To jest duża litera.")
elif litera.islower():
    print("To jest mała litera.")
else:
    print("To nie jest litera.")
