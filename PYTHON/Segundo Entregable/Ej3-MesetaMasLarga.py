def mesetaMasLarga(l: list[int]) -> int:
    mesetaMasLarga: int = 0
    largoDeMeseta: int = 1

    if len(l) == 0:
        return 0

    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            largoDeMeseta += 1
        else:
            mesetaMasLarga = max(mesetaMasLarga,largoDeMeseta)
            largoDeMeseta = 1
    mesetaMasLarga = max(mesetaMasLarga,largoDeMeseta)

    return mesetaMasLarga