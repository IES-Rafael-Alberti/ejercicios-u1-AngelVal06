# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. 
# Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. 
# Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. 
# Redondear cada cantidad a dos decimales.



usuario = input("Introduce tu usuario: ")

dinerodep = int(input("Introduce el dinero que depositará: "))

primer = 4*dinerodep / 100 + dinerodep

segundo = 0

tercero = 0

print(f"El usuario {usuario} ha depositado {dinerodep}")
print(f"La cantidad de ahorros del primer año ha sido {primer}€; la del segundo {segundo}€; y la del tercero {tercero}€")
