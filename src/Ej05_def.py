# recibe el importe del artículo sin iva y el tipo de iva a aplicar, pero no retorna nada, sino que se imprime desde dentro de la función.



def calcular_iva(importe, iva):
    preciofinal = (importe * iva / 100) + importe
    print(f"El precio final es de {preciofinal}€")



def main():
    importe = float(input("Dime el importe del artículo: "))
    iva = int(input("Dime el tipo de iva a aplicar: "))
    preciofinal = calcular_iva(importe, iva)



if __name__ == "__main__":
    main()







