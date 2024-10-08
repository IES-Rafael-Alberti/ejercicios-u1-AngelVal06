#Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio 
# final del artículo.

num1 = float(input("Dime el coste del artículo\n"))

num2 = float(input("Dime el porcentaje de IVA del artículo\n"))

num3 = num1 * num2 /100 + num1 

print(f"El precio final del artículo es {round(num3,2)} €")