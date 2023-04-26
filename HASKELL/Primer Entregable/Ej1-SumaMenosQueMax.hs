sumaMenosQueMax :: (Int, Int, Int) -> Bool
sumaMenosQueMax (a, b, c)
 | maximo (a, b, c) > (minimo (a, b, c) + medio (a, b, c)) = True
 | otherwise = False

maximo :: (Int, Int, Int) -> Int
maximo (a, b, c)
 | (a >= b) && (a >= c) = a
 | (b >= a) && (b >= c) = b
 | otherwise = c

minimo :: (Int, Int, Int) -> Int
minimo (a, b, c)
 | (a <= b) && (a <= c) = a
 | (b <= a) && (b <= c) = b
 | otherwise = c

medio :: (Int, Int, Int) -> Int
medio (a, b, c)
 | ((a <= b) && (b <= c)) || ((c <= b) && (b <= a)) = b
 | ((b <= a) && (a <= c)) || ((c <= a) && (a <= b)) = a
 | otherwise = c

