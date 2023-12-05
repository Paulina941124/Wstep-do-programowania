# Wartości początkowa i końcowa x oraz krok
xp = -4
xk = 4
krok = 0.5

# Wypisanie liczb z  zakresu z określonym krokiem

for x in range(int(xp * 2), int((xk + krok) * 2), int(krok * 2)):
    x1 = x/2.0
    y = 2*(x1**2)-5*x1-8
    print(f"Dla x równego {x1} wartość funkcji to {y}")
