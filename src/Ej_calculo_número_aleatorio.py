import random

def dame_un_número_aleatorio(min, max):
    return random.randint(min, max)

def main():
    print("Escribedos valores entre los que tenga que salir el número aleatorio")

    min = int(input("Dime el mínimo: "))
    max = int(input("Dime el máximo: "))

    num_random = dame_un_número_aleatorio(min, max)

    print(num_random)

if __name__ == "__main__":
    main()
