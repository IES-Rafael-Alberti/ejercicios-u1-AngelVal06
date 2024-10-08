# Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, 
# y muestre por pantalla cada uno de los productos en una línea distinta.



def lista(productos):
    i = 0
    while i < len(productos.split(",")):
        print(productos.split(", ")[i].title())
        i = i + 1

def main(): 
    productos = input("Dame una lista de la compra: ")
    lista(productos)

if __name__== "__main__":
    main()
