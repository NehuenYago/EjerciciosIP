-- Ejercicio 1
-- 1.1)
longitud :: [t] -> Integer
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

-- 1.2)
ultimo :: [t] -> t
ultimo [x] = x
ultimo (_:xs) = ultimo xs

-- 1.3)
principio :: [t] -> [t]
principio [x] = []
principio (x:xs) = x : principio xs

-- 1.4)
reverso :: [t] -> [t]
reverso [] = []
reverso (x:xs) = reverso xs ++ [x]

-- Ejercicio 2
-- 2.1)
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece e (x:xs)
 | e == x = True
 | otherwise = pertenece e xs

--  2.2)
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales [_] = True
todosIguales (x:xs) = x == head xs && todosIguales xs

-- 2.3)
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos (x:xs) = (not (pertenece x xs)) && todosDistintos xs

-- 2.4)
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs) = pertenece x xs || hayRepetidos xs

-- 2.4) otra forma
hayRepetidos2 :: (Eq t) => [t] -> Bool
hayRepetidos2 s = not (todosDistintos s)

-- 2.5)
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar e (x:xs)
 | e == x = xs
 | otherwise = x : quitar e xs

-- 2.6)
quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos e (x:xs)
 | e == x = quitarTodos e xs
 | otherwise = x : quitarTodos e xs

-- 2.7)
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) = x : (eliminarRepetidos (quitarTodos x xs))

-- 2.8)
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos x y = verificaMismosElementos x y && verificaMismosElementos y x

verificaMismosElementos :: (Eq t) => [t] -> [t] -> Bool
verificaMismosElementos [x] y = pertenece x y
verificaMismosElementos (x:xs) y = pertenece x y && verificaMismosElementos xs y

-- 2.9)
capicua :: (Eq t) => [t] -> Bool
capicua s = s == reverso s

-- 2.9) otra forma
capicua2 [] = True
capicua2 [_] = True
capicua2 (x:xs) = (x == ultimo xs) && capicua (eliminaUltimo xs) 

eliminaUltimo :: [t] -> [t]
eliminaUltimo [_] = []
eliminaUltimo (x:xs) = x : eliminaUltimo xs

-- Ejercicio 3
-- 3.1)
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

-- 3.2)
productoria :: [Integer] -> Integer
productoria [] = 1
productoria (x:xs) = x * productoria xs

-- 3.3)
maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x:xs)
 | x >= head xs = maximo (x : (tail xs))
 | otherwise = maximo xs

-- 3.4)
sumarN :: Integer -> [Integer] -> [Integer]
sumarN n [x] = (x + n) : []
sumarN n (x:xs) = (x + n) : sumarN n xs

-- 3.5)
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero (x:xs) = sumarN x (x:xs)

-- 3.6)
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo s = sumarN (ultimo s) s

-- 3.7)
pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs)
 | (mod x 2 == 0) = x : pares xs
 | otherwise = pares xs

--  3.8)
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN _ [] = []
multiplosDeN n (x:xs)
 | (mod x n == 0) = x : multiplosDeN n xs
 | otherwise = multiplosDeN n xs

-- 3.9)
ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar s = verificaOrden s s

verificaOrden :: [Integer] -> [Integer] -> [Integer]
verificaOrden [x] s = s
verificaOrden (x1:x2:xs) s
 | x1 <= x2 = verificaOrden (x2:xs) s
 | otherwise = ordenar (cambiaLugar s)

cambiaLugar :: [Integer] -> [Integer]
cambiaLugar [x] = [x]
cambiaLugar (x1:x2:xs)
 | x1 <= x2 = x1 : cambiaLugar (x2:xs)
 | otherwise = x2 : x1 : xs

-- 3.9) otra forma
ordenar2 :: [Integer] -> [Integer]
ordenar2 [] = []
ordenar2 (x:xs) = ordenar2Aux x (ordenar xs)

ordenar2Aux :: Integer -> [Integer] -> [Integer]
ordenar2Aux x [] = [x]
ordenar2Aux x (y:ys) 
    | x <= y = x : y : ys
    | otherwise = y : ordenar2Aux x ys

-- Ejercicio 4
-- 4.1)
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [c1] = [c1]
sacarBlancosRepetidos (c1:c2:cs)
 | (' ' == c1) && (c1 == c2) = sacarBlancosRepetidos (c1:cs)
 | otherwise = c1 : sacarBlancosRepetidos (c2:cs)

-- 4.2)
contarPalabras :: [Char] -> Integer
contarPalabras s = contarPalabrasAux (sacarRepetidos s)

contarPalabrasAux :: [Char] -> Integer
contarPalabrasAux [' '] = 0
contarPalabrasAux [c1] = 1
contarPalabrasAux (c1:c2:cs) 
 | c1 /= ' ' && c2 == ' ' = contarPalabrasAux (c2:cs)
 | c1 == ' ' && c2 /= ' ' = 1 + contarPalabrasAux (c2:cs)

sacarRepetidos :: [Char] -> [Char]
sacarRepetidos [c1] = [c1]
sacarRepetidos [] = []
sacarRepetidos (c1:c2:cs)
 | c1 == ' ' && c1 == c2 = sacarRepetidos (c2:cs)
 | c1 /= ' ' && c2 /= ' ' = sacarRepetidos (c2:cs)
 | otherwise = c1 : sacarRepetidos (c2:cs)

-- 4.3)
-- palabraMasLarga :: [Char] -> [Char]

-- buscaLetra :: [Char] 
-- buscaLetra (x:xs)
--  | x == ' ' = buscaLetra xs
--  | otherwise = concatenaPalabra (x:xs) : buscaEspacio xs

-- buscaEspacio (x:xs)
--  | x /= ' ' = buscaEspacio xs
--  | otherwise = 

-- concatenaPalabra :: [Char] -> []
-- concatenaPalabra [x] = [x]
-- concatenaPalabra (x:xs)
--  | x /= ' ' = x: concatenaPalabra xs
--  | x == ' ' = [] 

-- Ejercicio 5
-- 5.1)
nat2bin :: Integer -> [Integer]
nat2bin 0 = [0]
nat2bin 1 = [1]
nat2bin n = nat2bin (div n 2) ++ [mod n 2]

-- 5.2)
bin2nat :: [Integer] -> Integer
bin2nat [] = 0
bin2nat (x:xs) = x * (2 ^ (longitud(x:xs)-1)) + bin2nat xs