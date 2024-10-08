#Realiza un programa en Python que lea dos números enteros, muestre cuál es el menor de los dos y cuántos números existen entre ellos dos.

#  - El segundo número no puede ser igual, si es así, debe mostrar el error: **"Los números no pueden ser iguales"**.
#  - Si los números son diferentes, por ejemplo, 5 y 12, debe mostrar la frase: **"El número menor es el 5 y entre ellos existen 7 números enteros"**.


num1 = int(input("Dime un número: "))

num2 = int(input("Dime un número: "))

if(num1==num2):
    print("Error los números no pueden ser iguales.")
elif(num1 > num2):
    print(f"El número menor es el {num2} y entre ellos existen {num1 - num2} números enteros.")
else:
    print(f"El número menor es el {num1} y entre ellos existen {num2 - num1} números enteros.")
