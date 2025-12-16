# Paso 1: Pedir entradas
usuario = input("Ingrese el nombre de usuario: ")
dominio = input("Ingrese el dominio: ")

# Paso 2: Construir el correo usando join()
correo = "@".join([usuario, dominio])

# Paso 3: Mostrar resultado
print("El correo electrónico es:", correo)