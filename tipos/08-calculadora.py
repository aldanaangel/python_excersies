import math

primer_numero = input("Ingrese el primer valor ")
segundo_numero = input("Ingrese el segundo valor ")

primer_numero = int(primer_numero)
segundo_numero = int(segundo_numero)

suma = primer_numero + segundo_numero
resta = primer_numero - segundo_numero
multi = primer_numero * segundo_numero
div = primer_numero / segundo_numero

mensaje = f"""
Para los numeros {primer_numero} y {segundo_numero},
el resultado de la suma es {suma},
el resultado de la resta es {resta}
el resultado de la multiplicacion es {multi}
el resultado de la division es {div}
"""

print(mensaje)
