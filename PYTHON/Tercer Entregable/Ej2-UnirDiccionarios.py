from typing import List
from typing import Dict

def unir_diccionarios(a_unir: List[Dict[str,str]]) -> Dict[str,List[str]]:
    diccionarioNuevo: Dict() = {}

    for i in a_unir:
        items = i.items()
        print(items)


test = [{'a':'1', 'b':'2'},{'b':'3', 'c':'4'},{'a':'5'}]
unir_diccionarios(test)