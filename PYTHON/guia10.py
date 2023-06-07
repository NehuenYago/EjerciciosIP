f = open("/home/yago/Documents/repos/IP/PYTHON/input.txt","r")

# Ejercicio 1
# 1.1)
def contarLineas(archivo:str) -> int:
    l: int = 0
    for i in archivo.readlines():
        l += 1
    return l

# 1.2)
def existePalabra(palabra:str, archivo:str) -> bool:
    return palabra in archivo.read().split()

# 1.3)
def cantidadApariciones(palabra:str, archivo:str) -> int:
    texto = archivo.read()
    apariciones: int = 0

    for i in texto.split():
        if i == palabra:
            apariciones += 1
    return apariciones

# Ejercicio 2
# def clonarSinComentarios(archivo:str):
    