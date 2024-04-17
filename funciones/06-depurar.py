def calcular_largo_texto(texto):
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado


largo = calcular_largo_texto("Hola Mundo")
print(largo)
