# recibe horas y coste y retorna el importe total.


def comprueba_horas(valor):
    while (valor < 0):
        print("Dime las horas bien.")
        valor = int(input("Dime el número de horas: "))
    return valor

    
def comprueba_coste(valor):
    while (valor < 0):
        print("Dime las horas bien.")
        valor = int(input("Dime el coste por hora: "))
    return valor


def importe_total(horas, coste):
    importe = horas * coste
    return importe




def main():
    horas = int(input("Dime el número de horas: "))
    horas = comprueba_horas(horas)
    coste = int(input("Dime el coste por hora: "))
    coste = comprueba_coste(coste)
    importe = importe_total(horas, coste)
    print(f"Las horas de trabajo son {horas}")
    print(f"Coste por horas es de {coste}€")
    print(f"Importe total es de {importe}€")





if __name__ == "__main__":
    main()




