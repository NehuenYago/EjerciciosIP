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
    if palabra in texto:
        return True
    return False
