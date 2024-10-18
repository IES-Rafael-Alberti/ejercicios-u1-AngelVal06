# Realiza un programa en Python que pida un número de inicio, un incremento y un total de la serie.

#   - El incremento y el total deben ser mayores que cero. Si no es así, el programa debe finalizar con un error o obligar a que introduzcan un 
# valor correcto para ambos *(os lo dejo a vuestra elección, la primera opción es más fácil, aunque el mundo está lleno de valientes)*.

#   - Por ejemplo, si introducen los valores 1, 1 y 10, el programa mostrará en consola exactamente lo siguiente: 
# ***SERIE => 1-2..3..4..5..6..7..8..9-10***




def comprueba_incremento(valor):
    while (valor <= 0):
        print("Debe ser mayor a cero")
        valor = int(input("Dime el incremento: "))
    return valor



def comprueba_total(valor):
    while (valor <= 0):
        print("Debe ser mayor a cero")
        valor = int(input("Dime el total: "))
    return valor


def comprobar_serie(valor):

def main():
    Incremento = int(input("Dime el incremento: "))
    Incremento = comprueba_incremento(Incremento)
    total = float(input("Dime el total: "))
    total = comprueba_total(total)






if __name__ == "__main__":
    main()