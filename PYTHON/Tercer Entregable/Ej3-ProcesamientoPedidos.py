from queue import Queue
from typing import List
from typing import Dict
from typing import Union

# ACLARACIÓN: El tipo de "pedidos" debería ser: pedidos: Queue[Dict[str, Union[int, str, Dict[str, int]]]]
# Por no ser soportado por la versión de CMS, usamos simplemente "pedidos: Queue"
def procesamiento_pedidos(pedidos: Queue,
                          stock_productos: Dict[str, int],
                          precios_productos: Dict[str, float]) -> List[Dict[str, Union[int, str, float, Dict[str, int]]]]:
    
    pedidos_procesados:List[Dict[str, Union[int, str, float, Dict[str, int]]]] = []
    pedido_procesado: Dict[str, Union[int, str, float, Dict[str, int]]] = {}

    for i in range(len(pedidos)):
        productos: Dict[str,int] = pedidos[i].get('productos')
        precio_total:int = 0
        estado:str = 'completo'
        for producto in productos:
            while stock_productos.get(producto) > 0 and productos.get(producto) > 0:
                precio_total += precios_productos.get(producto)
                stock_productos[producto] -= 1
                productos[producto] -= 1
                                
            if productos.get(producto) > 0:
                estado = 'incompleto'
            
        # pedido_procesado = []
        pedidos_procesados += [pedido_procesado]

    return pedidos_procesados


pedidos = [{"id":21,"cliente":"Gabriela", "productos":{"Manzana":2}}, {"id":1,"cliente":"Juan","productos":{"Manzana":2,"Pan":4,"Factura":6}}]
stock_productos = {"Manzana":10, "Leche":5, "Pan":3, "Factura":0}
precios_productos = {"Manzana":3.5, "Leche":5.5, "Pan":3.5, "Factura":5}
print(procesamiento_pedidos(pedidos, stock_productos, precios_productos))