# Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.

num1 = float(input("Dime cuantos grados Celsius quieres que convierta: "))

num2 = num1 * 9 / 5 + 32

print(f"{round(num2,2)}ºF ({num1}ºC)")