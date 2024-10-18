# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y 
# el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.



fecha = input("Dime tu fecha de nacimiento con este formato dd/mm/aaaa: ")

dia = fecha.split("/")[0]
mes = fecha.split("/")[1]
año = fecha.split("/")[2]

print(f"Tu día de nacimiento es {dia}; tu mes {mes}; tu año {año}")
