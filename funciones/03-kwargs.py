# kwargs crea un diccionario de llave valor con los argumentos que se le pasan a la funcion sin
# necesidad de definirlos como parametros dentro de la misma. Se activa usando **

def get_product(**datos):
    print(f"{datos["id"]} {datos["product"]}")


get_product(id="01", product="IPhone", desc="Equipo celular.")
