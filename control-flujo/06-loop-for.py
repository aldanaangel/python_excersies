buscar = 10

for numero in range(5):
    print(numero)
    if numero == buscar:
        print('Encontre el valor:', buscar)
        break
else:
    print('Valor no encontrado.')

# Los strings tambien son iterables

for char in "Angel Aldana":
    print(char)
