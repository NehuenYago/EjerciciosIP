-- Ejercicio 1
-- 1)
longitud :: [t] -> Integer
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

-- 2)
ultimo :: [t] -> t
ultimo [x] = x
ultimo (_:xs) = ultimo xs

-- 3)
principio :: [t] -> [t]
principio [x] = []
principio (x:xs) = x : principio xs

-- 4)
reverso :: [t] -> [t]
reverso [] = []
reverso (x:xs) = reverso xs ++ [x]
