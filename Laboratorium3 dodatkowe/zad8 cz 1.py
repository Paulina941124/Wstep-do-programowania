lista = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","w","x","y","z"]
print(lista)
n = int(input("Podaj ile elementów ma zawierac lista:"))

podlisty = []

for i in range(0, len(lista), n):
    podlisty.append(lista[i:i + n])
print(podlisty)
