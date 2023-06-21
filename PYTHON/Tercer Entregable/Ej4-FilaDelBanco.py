from queue import Queue

# El tipo de fila debería ser Queue[int], pero la versión de python del CMS no lo soporta. Usaremos en su lugar simplemente "Queue"
def avanzarFila(fila: Queue, min: int):
    cantidadInicial = fila.qsize()
    minutos: int = 0

    minutoAtiendeCaja1 = 1
    minutoAtiendeCaja2 = 3
    minutoAtiendeCaja3 = 2
    minutoVuelveFilaCliente = 5
    clienteDeCaja3 = 0

    while minutos <= min:
        if minutoVuelveFilaCliente == minutos:
            fila.put(clienteDeCaja3)
            minutoVuelveFilaCliente += 3
            
        if minutos % 4 == 0:
            fila.put(cantidadInicial + 1)
            cantidadInicial += 1           

        if minutos == minutoAtiendeCaja1:
            if fila.empty():
                minutoAtiendeCaja1 += 1
            else:
                fila.get()
                minutoAtiendeCaja1 += 10

        if minutos == minutoAtiendeCaja2:
            if fila.empty():
                minutoAtiendeCaja2 += 1
            else:
                fila.get()
                minutoAtiendeCaja2 += 4

        if minutos == minutoAtiendeCaja3:
            if fila.empty():
                minutoAtiendeCaja3 += 1
                minutoVuelveFilaCliente += 1
            else:
                clienteDeCaja3 = fila.get()
                minutoAtiendeCaja3 += 4


        minutos += 1

    return fila


def cola(p):
    cola: Queue = Queue()
    for i in p:
        cola.put(i)
    return cola

print(list(avanzarFila(cola([1,2,3]), 14).queue))

# Caja1: Empieza a atender 10:01, y atiende a una persona cada 10 minutos
# Caja2: Empieza a atender 10:03, atiende a una persona cada 4 minutos
# Caja3: Empieza a atender 10:02, y atiende una persona cada 4 minutos, pero no le resuelve el problema y la persona debe volver a la fila (se va al final y tarda 3 min en llegar. Es decir, la persona que fue atendida 10:02 vuelve a entrar a la fila a las 10:05)
# La fila empieza con las n personas que llegaron antes de que abra el banco. Cuando abre (a las 10), cada 4 minutos llega una nueva persona a la fila (la primera entra a las 10:00)
