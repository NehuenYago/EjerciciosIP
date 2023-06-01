def mesetaMasLarga(l: list[int]) -> int:
    longitudMesetas: list[int] = []
    largoDeMeseta: int = 1

    if len(l) == 0:
        return 0

    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            largoDeMeseta += 1
        else:
            longitudMesetas.append(largoDeMeseta)
            largoDeMeseta = 1
    longitudMesetas.append(largoDeMeseta)

    return masLarga(longitudMesetas)

def masLarga(l:list[int]) -> int:
    n:int = 0
    for i in l:
        if i >= n:
            n = i
    return n 
