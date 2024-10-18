





def pasar_celsius_a_farenheit(farenheit: float) -> float:
    celsius = (farenheit - 32) * 5 / 9
    return  round(celsius, 2)


def main():
    farenheit = float(input("Dime los grados farenheit: "))
    celsius = pasar_celsius_a_farenheit(farenheit)
    print(celsius)


if __name__ == "__main__":
    main()





