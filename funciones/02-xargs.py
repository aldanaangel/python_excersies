# xargs genera un objeto iterable de todos los argumentos que se le pasen a la funcion sin
# necesidad de definirlos como parametros de la misma. Se activa usando el simbolo *

# def suma(a, b):
#     print(a + b)

# suma(3, 7)


def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero

    print(resultado)


suma(23, 20)
suma(4, 9, 5)
suma(3, 7, 8, 30, 6)
