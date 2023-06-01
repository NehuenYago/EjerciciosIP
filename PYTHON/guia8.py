# Ejercicio 1
# 1.1) Si se implementa con tipos genericos sirve para buscar un caracter en una string
def pertenece (s:list, e:int) -> bool:
    for i in s:
        if i == e:
            return True
    return False

# 1.2)
def divideATodos (s:list, e:int) -> bool:
    for i in s:
        if not i % e == 0:
            return False
    return True

# 1.3)
def sumaTotal (s:list) -> int:
    total: int = 0
    for i in s:
        total += i
    return total

# 1.4)
def ordenados (s:list) -> bool:
    for i in range(len(s)-1):
        if not s[i] < s[i+1]:
            return False
    return True

# 1.5)
def palabraLarga (s:list) -> bool:
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
def borraEnPares (lista:list) -> list:
    switch: bool = True
    
    for l in range(len(lista)):
        if switch:
            lista[l] = 0
        switch = not switch
    return lista
