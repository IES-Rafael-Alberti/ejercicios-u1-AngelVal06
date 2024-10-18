
def calcular_iva(importe: float, iva: float) -> str:
    if (iva < 1 or iva > 100):
        iva = 21
    preciofinal = (importe * iva / 100) + importe
    return f"El precio final del artículo con IVA ({iva:.2f}) es {preciofinal:.2f}€."




def main():
    importe = float(input("Dime el importe del artículo: "))
    iva = int(input("Dime el tipo de iva a aplicar: "))
    preciofinal = calcular_iva(importe, iva)
    print(preciofinal)



if __name__ == "__main__":
    main()




