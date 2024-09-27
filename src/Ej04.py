# Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.

num1 = int(input("Dime cuantos grados Celsius quieres que convierta"))

num2 = num1 * 9 / 5 + 32

print(f"{num1} son {num2} Fahrenheit")