from typing import List

def filasParecidas(matriz: List[List[int]]) -> bool:
    n:int = 0

    if len(matriz) == 1:
        return True
    elif len(matriz) > 1:
        n = matriz[1][0] - matriz[0][0]
    
    for i in range(1,len(matriz)):
        for j in range(len(matriz[i])):
            if not (matriz[i][j] == matriz[i-1][j] + n):
                return False
    return True
