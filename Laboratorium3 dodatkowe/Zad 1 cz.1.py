zdanie = input("Podaj zdanie: ")

zdanie1 = zdanie.lower()

litery = set(zdanie1)

litery_kolejno = sorted(litery)
print("Litery użyte w zdaniu to: ", litery_kolejno)

alfabet = {"a", "ą", "b", "c", "ć", "d", "e", "f", "g", "h", "i", "j", "k", "l", "ł", "m", "n", "ń", "o", "ó", "p", "r", "s", "t", "u", "w", "x", "y", "z"}

print("Pozostałe litery to: ", sorted(alfabet - litery))
