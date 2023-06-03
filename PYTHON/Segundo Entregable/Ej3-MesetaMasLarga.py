def mesetaMasLarga(l: list[int]) -> int:
    laMasLarga: int = 0
    largoDeMeseta: int = 1

    if len(l) == 0:
        return 0

    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            largoDeMeseta += 1
        else:
            laMasLarga = max(laMasLarga,largoDeMeseta)
            largoDeMeseta = 1
    laMasLarga = max(laMasLarga,largoDeMeseta)

    return laMasLarga