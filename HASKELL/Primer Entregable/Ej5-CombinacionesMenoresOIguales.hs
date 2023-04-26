combinacionesMenoresOiguales :: Integer -> Integer
combinacionesMenoresOiguales n = combinacionesAux n n n

combinacionesAux :: Integer -> Integer -> Integer -> Integer
combinacionesAux _ 1 _ = 1
combinacionesAux k n m = combinacionesAux2 k n m + combinacionesAux2 k n (m - 1) + combinacionesAux k (n - 1) (m - 1)

combinacionesAux2 :: Integer -> Integer -> Integer -> Integer
combinacionesAux2 _ _ 1 = 1
combinacionesAux2 k n m = comparar k (n * m) + combinacionesAux2 k n (m - 1)

comparar :: Integer -> Integer -> Integer
comparar k n
 | n <= k = 1
 | otherwise = 0

