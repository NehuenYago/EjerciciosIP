import math as math

# Ejercicio 1
# 1.1)
def raizDe2() -> float:
    return round(math.sqrt(2), 4)

# 1.2)
def imprimirHola():
    print("hola")

# 1.3)
def imprimirUnVerso():
    print("Around the World, around the wooorld!\n")

# 1.4)
def factorial2() -> int:
    return 2

# 1.5)
def factorial3() -> int:
    return 3 * factorial2()

# 1.6)
def factorial4() -> int:
    return 4 * factorial3()

# 1.7)
def factorial5() -> int:
    return 5 * factorial4()

# Ejercicio 2
# 2.1)
def imprimirSaludo(nombre: str):
    return print("Hola " + nombre)

# 2.2)
def raizCuadradaDe(numero: int) -> float:
    return math.sqrt(numero)

# 2.3)
def imprimirDosVeces(estribillo: str):
    print (estribillo * 4)
estribillo = "Around the world, around the wooorld!\n"

# 2.4)
def esMultiploDe(n: int, m: int) -> bool:
    if n%m == 0:
        return True
    else:
        return False

# 2.5)
def esPar(numero: int) -> bool:
    return esMultiploDe(numero, 2)

# 2.6)
def cantidadDePizzas(comensales: int, cantDePorciones: int) -> int:
    return math.ceil((cantDePorciones * comensales) / 8)

# Ejercicio 3
# 3.1)
def algunoEsCero(numero1: int, numero2: int) -> bool:
    return (numero1 == 0) or (numero2 == 0)

# 3.2)
def ambosSonCero(numero1: int, numero2: int) -> bool:
    return (numero1 == 0) and (numero2 == 0)

# 3.3)
def esNombreLargo(nombre: str) -> bool:
    longitud = len(nombre)
    return longitud >= 3 and longitud <= 8

# 3.4)
def esBisiesto(year: int) -> bool:
    return esMultiploDe(year, 400) or (esMultiploDe(year, 4) and not esMultiploDe(year, 100))

# Ejercicio 4
# 4.1)
def pesoPino(altura: int) -> int:
    if altura <= 300:
        return altura * 3
    else:
        return 900 + ((altura - 300) * 2)

# 4.2)
def esPesoUtil(peso: int) -> bool:
    return peso >= 400 and peso <= 1000

# 4.3) 4.4)
def sirvePino(altura: int) -> bool:
    return esPesoUtil(pesoPino(altura))
