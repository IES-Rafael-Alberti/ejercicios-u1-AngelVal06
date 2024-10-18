# Recibe un nombre y retorna una cadena de caracteres con el resultado.




def main():
    nombre = input("Escribe tu nombre: ")
    nombre = hola_nombre(nombre)
    print(nombre)


def hola_nombre(nombre):
    return "Hola, " + nombre


if __name__ == "__main__":
    main()

