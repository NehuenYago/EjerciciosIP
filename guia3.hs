-- Ejercicio 1
f :: Integer -> Integer
f n | n == 1 = 8
    | n == 4 = 131
    | n == 16 = 16

-- con Pattern Matching
-- f 1 = 8
-- f 4 = 131
-- f 16 = 16

g :: Integer -> Integer
g n | n == 8 = 16
    | n == 16 = 4
    | n == 131 = 1

-- Llamar a h hace fog
h :: Integer -> Integer
h n = f (g n)

-- Llamar a k hace gof
k :: Integer -> Integer
k n = g (f n)

-- Ejercicio 2 
-- a)
absoluto :: Integer -> Integer
absoluto n 
 | n < 0 = n * (-1)
 | n >= 0 = n

-- b)
maximoAbsoluto :: Integer -> Integer -> Integer
maximoAbsoluto x y
 | absoluto x >= absoluto y = x
 | otherwise = y

-- c)
maximo2 :: Integer -> Integer -> Integer
maximo2 x y
 | x >= y = x
 | otherwise = y

maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 x y z = maximo2 (maximo2 x y) z

-- d)
algunoEs0 :: Float -> Float -> Bool
algunoEs0 x y
 | x == 0 || y == 0 = True
 | otherwise = False

-- con Pattern Matching
algunoEs0PM :: Float -> Float -> Bool
algunoEs0PM 0 _ = True
algunoEs0PM _ 0 = True
algunoEs0PM _ _ = False

-- e)
ambosSon0 :: Float -> Float -> Bool
ambosSon0 x y
 | x == 0 && y == 0 = True
 | otherwise = False

-- con Pattern Matching
ambosSon0PM :: Float -> Float -> Bool
ambosSon0PM 0 0 = True
ambosSon0PM _ _ = False

-- f)
mismoIntervalo :: Float -> Float -> Bool
mismoIntervalo x y
 | x <= 3 && y <= 3 = True
 | (x > 3 && x <= 7) && (y > 3 && y <= 7) = True
 | x > 7 && y > 7 = True
 | otherwise = False

-- g)
sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos x y z
 | (x == y) && (y == z) = x
 | (x == y) || (x == z) = y + z
 | (y == z) = x + y
 | otherwise = x + y + z

-- h)
esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe x y
 | x < y = False
 | mod x y == 0 = True
 | otherwise = False

-- i) 
digitoUnidades :: Integer -> Integer
digitoUnidades x = mod x 10

-- j)
digitoDecenas :: Integer -> Integer
digitoDecenas x = div (mod x 100) 10