f = open("/home/yago/Documents/repos/IP/PYTHON/input.txt","r")

# Ejercicio 1
# 1.1)
def contarLineas(archivo:str) -> int:
    lineas = archivo.readlines()
    l: int = 0
    for i in lineas:
        l += 1
    return l

# 1.2)
def existePalabra(palabra:str, archivo:str) -> bool:
    texto = archivo.read()
    for i in texto.split():
        if i == palabra:
            return True
    return False

# 1.3)
def cantidadApariciones(archivo:str, palabra:str) -> int:
    texto = archivo.read()
    apariciones: int = 0
    for i in texto.split():
        if i == palabra:
            apariciones += 1
    return apariciones
