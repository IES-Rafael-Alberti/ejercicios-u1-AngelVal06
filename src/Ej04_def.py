# NO recibe parámetros y retorna una cadena de caracteres con la temperatura convertida en grados Celsius y entre parántesis la temperatura en grados farenheit... 
# ambas temperaturas con 2 posiciones decimales. Por ejemplo, si introduce 212 debe retornar la cadena "100.00ºC (212.00ºF)". 
# Dentro de la función se pedirá al usuario los grados Farenheit.


def pasar_celsius_a_farenheit():
    farenheit = float(input("Dime los grados farenheit: "))
    celsius = (farenheit - 32) * 5 / 9
    return  "%.2f" % celsius + "ºC (" + "%.2f" % farenheit + "ºF)"


def main():
    cadena = pasar_celsius_a_farenheit()
    print(cadena)


if __name__ == "__main__":
    main()


