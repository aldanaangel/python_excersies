
# Son contextos completamente diferentes, tanto el de las funciones como el global,
# por lo tanto se imprimen los diferentes mensajes segun sea el alcance.

saludo = "Hola Global"


def saludar():
    saludo = "Hola mundo"
    print(saludo)


def saludaChanchito():
    saludo = "Hola Chanchito"
    print(saludo)


saludar()
saludaChanchito()
print(saludo)
