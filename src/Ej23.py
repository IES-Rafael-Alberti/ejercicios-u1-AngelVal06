# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico 
# con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.



frase = input("Dime tu correo electrónico: ")

user = (frase.split("@")[0])

print(f"{user}@ceu.es")