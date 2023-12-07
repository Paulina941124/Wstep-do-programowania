n = int(input("Podaj numer ostatniego wyrazu "))
a1 = int(input("Podaj pierwszy wyraz ciągu "))
r = int(input("Podaj różnicę ciągu "))

an = a1+(n-1)*r
if n <= 0:
    print("Numer wyrazu musi być liczbą naturalną")

elif n > 0:
    for i in range(a1, an+1, r):
        print(i)
