def es_palindromo(texto):
    texto = texto.lower()
    tamano_texto = len(texto)
    for iterable in range(tamano_texto):
        revert_iterable = (tamano_texto-1) - iterable
        if texto[iterable] == texto[revert_iterable]:
            return True
        else:
            return False


def eliminar_espacios(texto):
    index = 0
    texto_formateado = ''
    texto_restante = ''

    for char in texto:
        if char == " ":
            if texto_formateado == "":
                texto_formateado = texto[:index]
            texto_formateado += texto[len(texto_formateado):]

            print(texto_formateado)

        index += 1


# print("Reconocer", es_palindromo("Reconocer"))
# print("Amo la paloma", es_palindromo("Amo la paloma"))
# print("Hola Mundo", es_palindromo("Hola Mundo"))
# es_palindromo("hola")

eliminar_espacios('hola mundo bello')
