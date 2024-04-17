mensaje_inicial = """
Bienvenidos a la calculadora:
Para salir escribe Salir.
Las operaciones son suma, resta, multi,div.
"""
comando_operacion = ''
print(mensaje_inicial)

primer_numero_ingresado = input('Ingrese el numero:')
primer_numero_ingresado = int(primer_numero_ingresado)

comando_operacion = input('Ingrese operacion:')

segundo_numero_ingresado = input('Ingrese el siguiente numero:')
segundo_numero_ingresado = int(segundo_numero_ingresado)

while comando_operacion.lower() != 'salir':
    if comando_operacion == 'suma':
        resultado_operacion = primer_numero_ingresado + segundo_numero_ingresado
    elif comando_operacion == 'resta':
        resultado_operacion = primer_numero_ingresado - segundo_numero_ingresado
    elif comando_operacion == 'multi':
        resultado_operacion = primer_numero_ingresado * segundo_numero_ingresado
    elif comando_operacion == 'div':
        resultado_operacion = primer_numero_ingresado / segundo_numero_ingresado
    else:
        resultado_operacion = 'Operacion no encontrada.'
        break

    print(f'el resultado es {resultado_operacion}')

    comando_operacion = input('Ingrese operacion:')
    if comando_operacion.lower() == 'salir':
        break
    segundo_numero_ingresado = input('Ingrese el siguiente numero:')
    segundo_numero_ingresado = int(segundo_numero_ingresado)
    primer_numero_ingresado = resultado_operacion
