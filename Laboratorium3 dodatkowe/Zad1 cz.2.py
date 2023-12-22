lista = []
while True:
    cyfry_uzytk = input("Podaj 5 cyfr rozdzielonych przecinkiem: ")
    cyfry = cyfry_uzytk.split(',')
    if len(cyfry) != 5:
        print("To nie 5 cyfr")
    else:
        lista = [int(cyfra) for cyfra in cyfry]
        break

print("Podane cyfry:", lista)
# not ready
