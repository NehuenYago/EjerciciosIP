from queue import Queue
from typing import List
from typing import Dict
from typing import Union

# ACLARACIÓN: El tipo de "pedidos" debería ser: pedidos: Queue[Dict[str, Union[int, str, Dict[str, int]]]]
# Por no ser soportado por la versión de CMS, usamos simplemente "pedidos: Queue"
def procesamiento_pedidos(pedidos: Queue,
                          stock_productos: Dict[str, int],
                          precios_productos: Dict[str, float]) -> List[Dict[str, Union[int, str, float, Dict[str, int]]]]:
    
    lista_pedidos_procesados = []

    while not pedidos.empty():
        pedido = pedidos.get()
        pedido_procesado = {}
        productos = pedido.get("productos")
        productos_recibidos = {}
        precio_total = 0
        estado = "completo"

        for producto in productos:
            cantidad_recibida = 0
            while stock_productos.get(producto) > 0 and productos.get(producto) > 0:
                precio_total += precios_productos.get(producto)
                stock_productos[producto] -= 1
                productos[producto] -= 1
                cantidad_recibida += 1
                                
            productos_recibidos[producto] = cantidad_recibida

            if productos.get(producto) > 0:
                estado = "incompleto"
        
        pedido_procesado["id"] = pedido.get("id")
        pedido_procesado["cliente"] = pedido.get("cliente")
        pedido_procesado["productos"] = productos_recibidos
        pedido_procesado["precio_total"] = precio_total
        pedido_procesado["estado"] = estado

        lista_pedidos_procesados.append(pedido_procesado)

    return lista_pedidos_procesados


def cola(p):
    cola: Queue = Queue()
    for i in p:
        cola.put(i)
    return cola

pedidos = [{"id":21,"cliente":"Gabriela", "productos":{"Manzana":2}}, {"id":1,"cliente":"Juan","productos":{"Manzana":2, "Pan":1,"Manzana":10}}]
stock_productos = {"Manzana":9, "Leche":5, "Pan":3, "Factura":0}
precios_productos = {"Manzana":3.5, "Leche":5.5, "Pan":3.5, "Factura":5}
print(procesamiento_pedidos(cola(pedidos), stock_productos, precios_productos))