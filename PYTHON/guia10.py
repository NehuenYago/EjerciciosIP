f = "/home/yago/Documents/repos/IP/PYTHON/input.txt"

# Ejercicio 1
# 1.1)
def contarLineas(filePath:str) -> int:
    archivo = open(filePath, "r")
    l: int = 0
    for i in archivo.readlines():
        l += 1
    return l

# 1.2)
def existePalabra(palabra:str, filePath:str) -> bool:
    archivo = open(filePath, "r")
    return palabra in archivo.read().split()

# 1.3)
def cantidadApariciones(palabra:str, filePath:str) -> int:
    archivo = open(filePath, "r")
    texto = archivo.read()
    apariciones: int = 0

    for i in texto.split():
        if i == palabra:
            apariciones += 1
    return apariciones

# Ejercicio 2
def clonarSinComentarios(filePath:str):
    archivo = open(filePath, "r")
    nuevoArchivo = open("newFile.txt", "w")

    for i in archivo.readlines():
        if i.split() == []:
            nuevoArchivo.write('\n')
        elif i.split()[0] != "#":
            nuevoArchivo.write(i)

# Ejercicio 3 El archivo debe terminar con una newline
def reversoLineas(filePath:str):
    archivo = open(filePath, "r")
    nuevoArchivo = open("newFile.txt", "w")
    lineas: [str] = archivo.readlines()

    for i in range(len(lineas)-1,-1,-1):
        nuevoArchivo.write(lineas[i])

    return nuevoArchivo

# Ejercicio 4
def agregaFraseAlFinal(frase:str, filePath:str):
    texto = open(filePath, "a")
    texto.write('\n')
    texto.write(frase)
    return texto
