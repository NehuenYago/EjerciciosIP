from queue import Queue

def procesamiento_pedidos(pedidos: Queue[dict[str, [int, str, dict[str, int]]]],
                          stockProductos: dict[str, int],
                          preciosProductos: dict[str, float]) -> list[dict[str, [int, str, float, dict[str, int]]]]:
    
    listaPedidosProcesados: list[dict[str, [int, str, float, dict[str, int]]]] = []

    while not pedidos.empty():
        pedido: dict[str, [int, str, dict[str, int]]] = pedidos.get()
        diccionarioProductos: dict[str, int] = pedido["productos"]
        precioTotal: int = 0
        estado: str = "completo"

        for producto in diccionarioProductos:
            cantidadRecibida: int = 0
            while stockProductos[producto] > 0 and diccionarioProductos[producto] > 0:
                precioTotal += preciosProductos[producto]
                stockProductos[producto] -= 1
                diccionarioProductos[producto] -= 1
                cantidadRecibida += 1
                                
            if diccionarioProductos[producto] > 0:
                estado = "incompleto"
            
            diccionarioProductos[producto] = cantidadRecibida
        
        pedido["productos"] = diccionarioProductos
        pedido["precio_total"] = precioTotal
        pedido["estado"] = estado

        listaPedidosProcesados.append(pedido)

    return listaPedidosProcesados
