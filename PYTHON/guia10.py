import random
from queue import LifoQueue as Pila

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
    lineas: list[str] = archivo.readlines()

    for i in range(len(lineas)-1,-1,-1):
        nuevoArchivo.write(lineas[i])

# Ejercicio 4
def agregaFraseAlFinal(frase:str, filePath:str):
    archivo = open(filePath, "a")
    archivo.write('\n')
    archivo.write(frase)

# Ejercicio 5
def agregaFraseAlComienzo(frase:str, filePath:str):
    archivo = open(filePath, "r")
    lineas: list[str] = archivo.readlines()

    archivo = open(filePath, "w")
    archivo.write(frase)
    archivo.write('\n\n')

    for l in lineas:
        archivo.write(l)

# Ejercicio 6
# def devuelveListaPalabras(filePath:str):
#     archivo = open(filePath, "rb")

# Ejercicio 7
def promedioEstudiante(lu:str, filePath:str) -> float:
    archivo = open(filePath, "r")
    lineas = archivo.readlines()
    libreta, nota, totalNotas, cantidadMaterias, promedio = 0,0,0,0,0

    for i in range(len(lineas)):
        sinNewline = lineas[i].strip('\n')
        libreta = int(sinNewline.split(',')[0])
        nota = int(sinNewline.split(',')[3])

        if libreta == int(lu):
            totalNotas += nota
            cantidadMaterias += 1
    
    if cantidadMaterias > 0:
        promedio = totalNotas / cantidadMaterias

    return promedio

# Ejercicio 8
def generarNumerosAlAzar(n:int, desde:int, hasta:int) -> list[int]:
    return random.sample(range(desde, hasta), n)

# Ejercicio 9 Para print pila hacer .queue
def armaPila(n:int, desde:int, hasta:int) -> Pila:
    pila: Pila = Pila()
    lista:list[int] = generarNumerosAlAzar(n, desde, hasta)

    for l in lista:
        pila.put(l)
        
    return pila

# Ejercicio 10
def cantidadElementos(p: Pila) -> int:
    return p.qsize()
