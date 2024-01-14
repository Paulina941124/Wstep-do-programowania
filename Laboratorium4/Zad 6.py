import math


def pole_trojkata(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        print("Boki trójkątów muszą być większe od 0")
    elif a + b > c and a + c > b and b + c > a:
        p = (a+b+c)/2
        pole = math.sqrt(p*(p-a)*(p-b)*(p-c))
        return pole
    else:
        print("Podano niepoprawne dane")


wynik = pole_trojkata(3, 4, 5)
print(f"Pole trójkąta wynosi {wynik}")
