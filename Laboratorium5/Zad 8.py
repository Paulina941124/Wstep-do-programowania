import math

def oblicz_pole_trojkata(bok_a, bok_b, kat_c):

    if bok_a + bok_b <= kat_c or bok_a + kat_c <= bok_b or bok_b + kat_c <= bok_a:
        print("Trójkąt o podanych bokach i kącie nie istnieje.")
        return None


    kat_c_rad = math.radians(kat_c)


    pole = 0.5 * bok_a * bok_b * math.sin(kat_c_rad)
    return pole

def czy_prostokatny(bok_a, bok_b, kat_c):

    if bok_a**2 + bok_b**2 == (bok_a + bok_b)**2:
        return True
    elif bok_a**2 + kat_c**2 == (bok_a + kat_c)**2:
        return True
    elif bok_b**2 + kat_c**2 == (bok_b + kat_c)**2:
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        bok_a = float(input("Podaj długość boku a: "))
        bok_b = float(input("Podaj długość boku b: "))
        kat_c = float(input("Podaj miarę kąta C w stopniach: "))

        pole = oblicz_pole_trojkata(bok_a, bok_b, kat_c)

        if pole is not None:
            print(f"Pole trójkąta wynosi: {pole:.2f}.")

            if czy_prostokatny(bok_a, bok_b, kat_c):
                print("Trójkąt jest prostokątny.")
            else:
                print("Trójkąt nie jest prostokątny.")
    except ValueError:
        print("Podano nieprawidłowe dane.")
