# Zadanie 6
def NWD(a, b):
    while b:
        a, b = b, a % b
    return a


print(NWD(33, 55))

# Zadanie 7


def palindrom(slowo):
    slowo = slowo.lower()
    odwrocone_slowo = slowo[::-1]
    return slowo == odwrocone_slowo


print(palindrom("kajak"))

# Zadanie 8


def anagram(c, d):
    c = c.lower()
    d = d.lower()
    return sorted(c) == sorted(d)


c = input("słowo c:")
d = input("słowo d:")

print(anagram(c, d))
