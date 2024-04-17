def hola(nombre, apellido="Valor por defecto"):  # Parametros
    print('Hola Mundo')
    print(f"Bienvenido {nombre} {apellido}")


hola("Angel", "Aldana")  # Argumentos
hola("David")
hola(apellido="Aldana", nombre='Angel')
