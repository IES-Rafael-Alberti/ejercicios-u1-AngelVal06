# Una panadería vende barras de pan a 3.49€ cada una. 
# El pan que no es del día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
# Después el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante), 
# el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas.



pan = int(input("Dime cuantas barras de pan que no son del día quieres\n"))

precio = 3.49

num = (pan * precio)*60 / 100

print(f"El descuento que se le hace son {round(num,2)}€; y el coste final es {round(pan*precio - num,2)}")
