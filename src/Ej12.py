# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales.


num1 = float(input("Dime tu peso en Kg\n"))

num2 = float(input("Dime tu altura en metros\n"))

num3 = num1 / (num2 ** 2)

num4 = round(num3, 2)

print(f"Tu índice de masa corporal es {num4}")