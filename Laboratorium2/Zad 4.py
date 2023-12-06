a = int(input("Podaj pierwszą liczbę "))
b = int(input("Podaj drugą liczbę "))

if a < b:
    for i in range(a, b+1):
        if i % 2 == 1:
            continue
        print(i)
elif a > b:
    for i in range(b, a+1):
        if i % 2 == 1:
            continue
        print(i)
