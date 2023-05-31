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

# Ejercicio 5
# 5.1)
def devolverElDobleSiEsPar(numero: int) -> int:
    if esPar(numero):
        return numero*2
    else: 
        return numero

# 5.2)
def devolverValorSiEsParSinoElQueSigue(numero: int) -> int:
    if esPar(numero):
        return numero
    else: 
        return numero+1

# 5.3)
def devolverElDobleSiEsMultiplo3TripleSiEsMultiplo9(numero: int) -> int:
    if esMultiploDe(numero, 9):
        return numero*3
    elif esMultiploDe(numero, 3):
        return numero*2
    else:
        return numero
    
def devolverElDobleSiEsMultiplo3TripleSiEsMultiplo9v2(numero: int) -> int:
    if esMultiploDe(numero, 3) and not esMultiploDe(numero, 9):
        return numero*2
    elif esMultiploDe(numero, 9):
        return numero*3
    else:
        return numero

# 5.4)
def longitudNombre(nombre: str):
    if len(nombre) >= 5:
        print("Tu nombre tiene muchad letras!")
    else:
        print("Tu nombre tiene menos de 5 caracteres")

# 5.5)
def vacacionesOTrabajo(edad: int, sexo: str):
    if sexo == "M":
        if edad < 18 or edad >= 65:
            print("Anda de vacaciones")
        else:
            print("Anda a trabajar")
    elif sexo == "F":
        if edad < 18 or edad >= 60:
            print("Anda de vacaciones")
        else:
            print("Anda a trabajar")
