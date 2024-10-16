# recibe un número y retorna una cadena de caracteres con el resultado de la función.




def calcular_número(valor):
    valor = valor*(valor+1)/2
    return f"El resultado es {valor}"


def main():
    numero = int(input("Dime un número: "))
    numero = calcular_número(numero)
    print(numero)


if __name__ == "__main__":
    main()








