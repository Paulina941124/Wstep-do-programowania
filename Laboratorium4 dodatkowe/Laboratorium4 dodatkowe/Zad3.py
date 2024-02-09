import math


def pierw_kwadrat(a, b, c):
    delta = b**2-4*a*c
    if delta < 0:
        return ()
    elif delta == 0:
        x1 = -b/(2*a)
        return (x1,)
    elif delta > 0:
        pierw_delta = math.sqrt(delta)
        x2 = (-b-pierw_delta)/(2*a)
        x3 = (-b+pierw_delta)/(2*a)
        return x2, x3


wynik = pierw_kwadrat(1,3, -10)

print(wynik)
