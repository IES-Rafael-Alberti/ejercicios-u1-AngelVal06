import math

def tiene_mas_de_un_punto(valor: str):
    pos_primer_punto = valor.find(".") >= 0
    if pos_primer_punto >= 0 and valor.find(".", pos_primer_punto + 1):
            return False
    else:
        return True



def contiene_solo_digitos_y_un_punto(valor: str):
    for i in range(len(valor)): # 0..len(valor)..1 - i
        if not valor[i].isdigit() or valor[i] == ".":
            return False



def comprobar_número_float(valor: str):
    if valor[:1] == ".":
        valor = valor[1:]
    
    if tiene_mas_de_un_punto(valor):
        return False
    
    return contiene_solo_digitos_y_un_punto(valor)

    
def calcular_area(lado_a, lado_b, lado_c):
    semiperímetro = (lado_a + lado_b + lado_c) / 2
    area = math.sqrt(semiperímetro * (semiperímetro - lado_a) * (semiperímetro - lado_b) * (semiperímetro - lado_c))
    return area


def introduce_número(msj: str):
    numero = input(msj).strip()
    while comprobar_número_float(numero) == False:
        print("**ERROR** Número Inválido")
        numero = input(msj).strip()
    
    return float(numero)


def main():
    print("Dame los tres lados de un triangulo...")

    lado_a = introduce_número("Lado 1: ")
    lado_b = introduce_número("Lado 2: ")
    lado_c = introduce_número("Lado 3: ")

    calcular_area(lado_a, lado_b, lado_c)


if __name__ == "__main__":
    main()