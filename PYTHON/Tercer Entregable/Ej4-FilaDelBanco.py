from queue import Queue

def avanzarFila(fila: Queue[int], min: int):
    cantidadInicial = fila.qsize()
    minutos: int = 0

    minutoVuelveFilaCliente:int = -1
    clienteDeCaja3:int = 0

    while minutos <= min:
            
        if minutos % 4 == 0:
            fila.put(cantidadInicial + 1)
            cantidadInicial += 1

        if minutoVuelveFilaCliente == minutos:
            fila.put(clienteDeCaja3)

        if minutos % 10 == 1 and not fila.empty():
            fila.get()

        if minutos % 4 == 3 and not fila.empty():
            fila.get()

        if minutos % 4 == 2 and not fila.empty():
            clienteDeCaja3 = fila.get()
            minutoVuelveFilaCliente = minutos + 3

        minutos += 1

    return fila
