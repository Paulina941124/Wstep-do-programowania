def pole_trapezu(a, b, h):
    if a > 0 and b > 0 and h > 0:
        print(((a+b)*h)/2)
    else:
        print("Żaden wymiar nie może być mniejszy lub równy 0.")


pole_trapezu(2,5,7)
