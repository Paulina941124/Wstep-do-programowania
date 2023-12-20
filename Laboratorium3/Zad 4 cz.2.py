import random
# ilość elementów zbioru X
a = random.randint(3, 7)
print(f"Ilość elementów zbioru X: {a}")

# ilość elementów zbioru Y
b = random.randint(3, 7)
print(f"Ilość elementówn zbioru Y: {b}")

# definiowanie list

listaX = random.sample(range(1, 10+1), a)
listaY = random.sample(range(1, 10+1), b)

# zamiana listy na zbiór

X = set(listaX)
Y = set(listaY)
print(f"Zbiór X to {X}")
print(f"Zbiór Y to {Y}")

# a)
print("Czy w zbiorze X jest 5?", 5 in X)
# b)
print("Czy zbiór X jest podzbiorem Y? ", X in Y)
# c)
print("Czy zbiór Y jest podzbiorem X? ", Y in X)
# d)
print("Czy zbiór X jest nadzbiorem zbioru Y?", X.issuperset(Y))
# e)
print("Czy zbiór Y jest nadzbiorem zbioru X?", Y.issuperset(X))
# f)
print("Suma zbiorów to ", X.union(Y))
# g,h)
print("X/Y= ", X.difference(Y))
print("Y/X= ", Y.difference(X))
# i)
print("Iloczyn zbiorów to: ", X.intersection(Y))
# j)
print("Różnica symetryczna zbiorów: ", X.symmetric_difference(Y))
# k)
print("Najwyższy element obu zbiorów to", max(X.union(Y)))
# l)
# wyznaczam pierwszy element zbioru X
x1 = min(X)
print(f"Pierwszy element zbioru X to {x1}")
X.remove(x1)
Y.add(x1)
print("Zbiory po zmianach:")
print(f"X= {X}")
print(f"Y= {Y}")
# m)
Y.update(X.copy())
print("Zbiór Y po dodaniu elementów X: ", Y)
# n)
print("Zbiory po usunięciu elementów.")
print("Zbiór X ", X.clear())
print("Zbiór Y ", Y.clear())

# skonczone
