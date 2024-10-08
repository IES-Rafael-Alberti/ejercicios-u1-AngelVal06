# Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado y 
# el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%).


num1 = float(input("Dime el importe final del artículo: \n"))

num2 = 10

num3 = num1 * num2 /100 - num1 

print(f"El precio inicial del artículo es {round(num3,2)} €")
