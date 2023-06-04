# Ejercicio 1
# 1.1) Si se implementa con tipos genericos sirve esPara buscar un caracter en una string
def pertenece (s:list[int], e:int) -> bool:
    for i in s:
        if i == e:
            return True
    return False

# 1.2)
def divideATodos (s:list[int], e:int) -> bool:
    for i in s:
        if not i % e == 0:
            return False
    return True

# 1.3)
def sumaTotal (s:list[int]) -> int:
    total: int = 0
    for i in s:
        total += i
    return total

# 1.4)
def ordenados (s:list[int]) -> bool:
    for i in range(len(s)-1):
        if not s[i] < s[i+1]:
            return False
    return True

# 1.5)
def palabraLarga (s:list[str]) -> bool:
    for i in s:
        if len(i) > 7:
            return True
    return False

# 1.6)
def esPalindroma (p:str) -> bool:
    i: int = 0
    while i < (len(p))/2:
        if p[i] != p[len(p)-1-i]:
            return False
        i += 1
    return True

# 1.7)
def analizarContraseña (c:str) -> str:
    if len(c) < 5:
        return "ROJA"
    elif len(c) > 8 and tieneMinMayusYNum(c):
        return "VERDE"
    else:
        return "AMARILLA"

def tieneMinMayusYNum (s:str) -> bool:
    tieneMin: bool = False
    tieneMayus: bool = False
    tieneNum: bool = False
    n: int = 0

    for i in s:
        if 'a'<=i<='z':
            tieneMin = True

        if 'A'<=i<='Z':
            tieneMayus = True

    while n < 10:
        for i in s:
            if i == str(n):
                tieneNum = True
        n += 1

    return (tieneMin and tieneMayus and tieneNum)

# 1.8)
def cuentaBancaria (transacciones:list[tuple]) -> int:
    saldo: int = 0
    for t in transacciones:
        if t[0] == 'I':
            saldo += t[1]
        elif t[0] == 'R':
            saldo -= t[1]
    return saldo

# 1.9)
def alMenosTresVocalesDistintas (palabra: str) -> bool:
    hayA:int = 0
    hayE:int = 0
    hayI:int = 0
    hayO:int = 0
    hayU:int = 0

    for p in palabra:
        if p == 'a':
            hayA = 1
        if p == 'e':
            hayE = 1
        if p == 'i':
            hayI = 1
        if p == 'o':
            hayO = 1
        if p == 'u':
            hayU = 1
    
    vocales: int = hayA + hayE + hayI + hayO + hayU
    return (vocales >= 3)

# Ejercicio 2
# 2.1)
def borraEnPares (lista:list[int]) -> list[int]:
    for i in range(len(lista)):
        if i%2 == 0:
            lista[i] = 0

    return lista

# 2.2)
def borraEnPares2 (lista:list[int]) -> list[int]:
    lista2: list = []

    for i in range(len(lista)):
        if i%2 == 0:
            lista2.append(0)
        else:
            lista2.append(lista[i])

    return lista2

# 2.3)
def sacaVocales (texto:str) -> str:
    textoSinVocales:str = ''
    for i in texto:
        if not (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            textoSinVocales += i
    return textoSinVocales

# 2.4)
def reemplazaVocales (s:str) -> str:
    s2:str = ''
    for i in s:
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            s2 += '_'
        else:
            s2 += i
    return s2

# 2.5)
def daVueltaStr (s:str) -> str:
    s2:str = ''
    for i in s:
        s2 = i + s2
    return s2

# Ejercicio 3
# 3.1)
def listaEstudiantes() -> list[str]:
    listaNombres: list[str] = []
    nombre: str = input('Ingresar nombre del estudiante: ')

    while nombre != 'listo':
        listaNombres.append(nombre)
        nombre = input('Ingresar nombre del estudiante: ')

    return print(listaNombres)
