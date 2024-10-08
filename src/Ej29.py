# Realiza un programa en Python que solicite un nombre y una edad.

#  - Si el nombre está vacío, debes utilizar el valor **"Desconocido"**. La edad debe pedirse hasta que introduzca una edad comprendida entre 
#    0 y 125 años.
#  - El programa mostrará la siguiente frase: **"Te llamas Pepito y tienes 20 años, te quedan aún 105 años por cumplir"**.


nombre = input("Dime tu nombre: ")
edad = int(input("Dime tu edad: "))

if nombre == "":
    nombre = "Desconocido"


while(edad > 125 or edad < 0):
    print("Pon una edad coherente")
    edad = int(input("Dime tu edad: "))


print(f"Te llamas {nombre} y tienes {edad}, te quedan {125 - edad} años por cumplir.")