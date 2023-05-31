# Ejercicio 1
# 1.1) Si se implementa con tipos genericos sirve para buscar una caracter en una string
def pertenece (s: list, e: int) -> bool:
    for i in range(len(s)):
        if s[i] == e:
            return True
    return False

# 1.2)
def divideATodos (s: list, e: int) -> bool:
    i = 0
    while i < len(s):
        if s[i] % e == 0:
            i += 1
        else:
            return False
    return True

# 1.3)
