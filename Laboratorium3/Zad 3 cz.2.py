slownik = {"styczeń": 320.85, "luty": 287.22, "marzec": 315.29, "kwiecień": 266.20, "maj": 350.88}

# a)

print("Najwyższy rachunek to: ", max(slownik.values()))
print("Najniższy rachunek to: ", min(slownik.values()))
suma = sum(slownik.values())
print("Suma rachunków to: ", suma)
srednia = suma/5
print(f"Średnia rachunków to {srednia}")

# b)
if srednia < 350.88:
    print("Zacznij oszczędzać!")
else:
    print("Jesteś bezpieczny.")
