# Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y 
# muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, 
# el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.




nombre_producto = input("Introduce el nombre del producto: ")
precio_unitario = float(input("Introduce el precio del producto: "))
numero_unidades = int(input("Introduce el número de unidades: "))

coste_total = precio_unitario * numero_unidades

print(f"{nombre_producto} {precio_unitario:>6} {numero_unidades:3d} {coste_total:8.2f}")


