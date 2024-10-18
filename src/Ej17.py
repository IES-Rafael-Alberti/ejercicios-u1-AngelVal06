# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas 
# el nombre del usuario tantas veces como el número introducido.

user = input("Escribe el usuario: ")

num = int(input("Escribe un número: "))

while(num>0):
    print(user)
    num = num - 1