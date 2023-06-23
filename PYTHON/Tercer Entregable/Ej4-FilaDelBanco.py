from queue import Queue

# El tipo de fila debería ser Queue[int], pero la versión de python del CMS no lo soporta. Usaremos en su lugar simplemente "Queue"
def avanzarFila(fila: Queue, min: int):
    cantidadInicial = fila.qsize()
    minutos: int = 0

    minutoVuelveFilaCliente:int = -1
    clienteDeCaja3 = 0

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


def cola(p):
    cola: Queue = Queue()
    for i in p:
        cola.put(i)
    return cola

print(list(avanzarFila(cola([1,2,3]), 100).queue))

# Caja1: Empieza a atender 10:01, y atiende a una persona cada 10 minutos
# Caja2: Empieza a atender 10:03, atiende a una persona cada 4 minutos
# Caja3: Empieza a atender 10:02, y atiende una persona cada 4 minutos, pero no le resuelve el problema y la persona debe volver a la fila (se va al final y tarda 3 min en llegar. Es decir, la persona que fue atendida 10:02 vuelve a entrar a la fila a las 10:05)
# La fila empieza con las n personas que llegaron antes de que abra el banco. Cuando abre (a las 10), cada 4 minutos llega una nueva persona a la fila (la primera entra a las 10:00)
