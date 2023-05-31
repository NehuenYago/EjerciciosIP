# Ejercicio 1
# 1.1) Si se implementa con tipos genericos sirve para buscar una caracter en una string
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
    total = 0
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
    i = 0
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
    n = 0

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
    saldo = 0
    for t in transacciones:
        if t[0] == 'I':
            saldo += t[1]
        elif t[0] == 'R':
            saldo -= t[1]
    return saldo

print(cuentaBancaria([('I', 2000), ('R',20),('R', 1000),('I', 300)]))
