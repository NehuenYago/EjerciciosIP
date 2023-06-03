def sePuedeLlegar(origen: str, destino: str, vuelos: list[tuple[str, str]]) -> int:
    longitudRuta: int = 0
    i: int = 0
    nuevoOrigen: str = origen

    while i < len(vuelos):
        if nuevoOrigen == vuelos[i][0]:
            longitudRuta += 1
            if destino == vuelos[i][1]:
                return longitudRuta
            if origen == vuelos[i][1]:
                return -1
            nuevoOrigen = vuelos[i][1]
            i = 0
            continue
        i += 1
    return -1