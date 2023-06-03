def quienGana (j1: str, j2: str) -> str:
    if j1 == j2:
        return "Empate"
    elif j1 == "Piedra":
        if j2 == "Papel":
            return "Jugador2"
        elif j2 == "Tijera":
            return "Jugador1"
    elif j1 == "Papel":
        if j2 == "Piedra":
            return "Jugador1"
        elif j2 == "Tijera":
            return "Jugador2"
    elif j1 == "Tijera":
        if j2 == "Piedra":
            return "Jugador2"
        elif j2 == "Papel":
            return "Jugador1"
