# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla 
# el número de euros y el número de céntimos del precio introducido.



precio = float(input("Dime el precio de un producto: "))

num1 = round(precio, 2)

num2 = num1 / 1 

num3 = num1 % 1

print(f"El número de € es {int(num2)} y el número de centimos es {round(num3,2)}")