from queue import LifoQueue

def calcularExpresion(expresion: str) -> float:
    pila: LifoQueue = LifoQueue()
    x: float = 0
    y: float = 0
    cuenta: float = 0
    expresion = expresion.split()
    
    for i in expresion:
        if i != '+' and i != '-' and i != '*' and i != '/':
            pila.put(i)
        else:
            if pila.qsize() > 1:
                x = pila.get()
                y = pila.get()
                cuenta = haceOperacion(i, float(x), float(y))
            else:
                y = pila.get()
                cuenta = haceOperacion(i, cuenta, float(y))
    
    return cuenta

def haceOperacion(signo: str, x:float, y:float) -> float:
    if signo == '+':
        return y + x
    elif signo == '-':
        return y - x
    elif signo == '*':
        return y * y
    elif signo == '/':
        return y / x
