# Ejercicio 1
# 1.1)
def pertenece (s: list, e: int) -> bool:
    for i in range(len(s)):
        if s[i] == e:
            return True
    return False
