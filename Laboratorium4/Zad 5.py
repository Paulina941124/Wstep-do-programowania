def bmi(waga, wzrost):

    if wzrost <= 0 or waga <= 0:
        return "Waga i wzrost muszą być dodatnie"

    bmi = waga / (wzrost ** 2)

    # Informacja zwrotna
    if bmi < 18.5:
        print("Masz niedowagę")
    elif 18.5 <= bmi < 24.9:
        print("Twoja waga jest prawidłowa")
    elif 25 <= bmi < 29.9:
        print("Masz nadwagę")
    else:
        print("Otyłość!")

    return bmi


waga = float(input("Podaj swoją wagę w kg: "))
wzrost = float(input("Podaj swój wzrost w metrach: "))

wynik = bmi(waga, wzrost)
print(f"Twoje BMI wynosi: {wynik}")
