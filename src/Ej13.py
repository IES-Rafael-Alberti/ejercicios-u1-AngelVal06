# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla los siguienteS: 
# "la división de n entre m da un cociente c y un resto r", donde n y m son los números introducidos por el usuario, y c y r son el cociente y el resto de la división entera respectivamente.

n = int(input("Dime un número\n"))

m = int(input("Dime un número\n"))

c = int(n / m)

r = n % m 

print(f"La división de {n} entre {m} da un cociente de {c} y un resto de {r}")