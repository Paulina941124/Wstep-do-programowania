def wspolne_wart(a, b):
    wspolne = set(a) & set(b)
    return wspolne

a = ["a", 2, "b", 5, 8, "g"]
b = [1, "a", 5, "k", 9, "z"]

print(list(wspolne_wart(a, b)))