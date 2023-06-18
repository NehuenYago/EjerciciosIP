def unirDiccionarios(aUnir: list[dict[str,str]]) -> dict[str,list[str]]:
    diccionarioNuevo: dict() = {}

    for i in aUnir:
        items = i.items()
        for tupla in items:
            if tupla[0] in diccionarioNuevo:
                diccionarioNuevo[tupla[0]] += [tupla[1]]
            else:
                diccionarioNuevo[tupla[0]] = [tupla[1]]
            
    return diccionarioNuevo
