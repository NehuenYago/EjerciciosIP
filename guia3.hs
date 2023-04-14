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
 | mod x y == 0 = True
 | otherwise = False

-- i) 
digitoUnidades :: Integer -> Integer
digitoUnidades x = mod x 10

-- j)
digitoDecenas :: Integer -> Integer
digitoDecenas x = div (mod x 100) 10

-- Ejercicio 3
-- la formula a*a + a*b*k = 0 se cumple cuando a+bk=0, o sea, cuando b es multiplo de a
estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados a b = esMultiplo a b

-- Ejercicio 4
-- a)
prodInt :: (Int, Int) -> (Int, Int) -> Int
prodInt x y = fst x * fst y + snd x * snd y

-- b)
todoMenor :: (Int, Int) -> (Int, Int) -> Bool
todoMenor x y
 | fst x == fst y && snd x == snd y = True
 | otherwise = False

--  c)
distanciaPuntos :: (Float, Float) -> (Float, Float) -> Float
distanciaPuntos x y = sqrt((fst x - fst y)^2 + (snd x - snd y)^2)

-- d)
sumaTerna :: (Float, Float, Float) -> (Float, Float, Float) -> (Float, Float, Float)
sumaTerna (x1, x2, x3) (y1, y2, y3) = (x1 + y1, x2 + y2, x3 + y3)

-- e)
sumarSoloMultiplos :: (Int, Int, Int) -> Int -> Int
sumarSoloMultiplos (x1, x2, x3) k = (esMultiploNum x1 k) + (esMultiploNum x2 k) + (esMultiploNum x3 k)

esMultiploNum :: Int -> Int -> Int
esMultiploNum x y
 | mod x y == 0 = x
 | otherwise = 0

-- f)
posPrimerPar :: (Integer, Integer, Integer) -> Integer
posPrimerPar (x1, x2, x3)
 | (esMultiploDe x1 2) == True = 1
 | (esMultiploDe x2 2) == True = 2
 | (esMultiploDe x3 2) == True = 3
 | otherwise = 4

-- g)
crearPar :: a -> b -> (a, b)
crearPar x y = (x, y)

-- h)
invertir :: (a, b) -> (b, a)
invertir (x, y) = (y, x)

-- Ejercicio 5
todosMenores :: Integer -> Integer -> Integer -> Bool
todosMenores x1 x2 x3
 | ((f5 x1 > g5 x1) && (f5 x2 > g5 x2) && (f5 x3 > g5 x3)) == True = True
 | otherwise = False

f5 :: Integer -> Integer
f5 n
 | n <= 7 = n^2
 | n > 7 = 2*n - 1

g5 :: Integer -> Integer
g5 n
 | esPar n == True = div n 2
 | otherwise = 3*n + 1

esPar :: Integer -> Bool
esPar x
 | mod x 2 == 0 = True
 | otherwise = False

-- Ejercicio 6
bisiesto :: Integer -> Bool
bisiesto a
 | ((not (esMultiplo a 4)) || (esMultiplo a 100) && (not (esMultiplo a 400))) == True = False
 | otherwise = True

esMultiplo :: Integer -> Integer -> Bool
esMultiplo x y
 | mod x y == 0 = True
 | otherwise = False

-- Ejercicio 7
distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (p1, p2, p3) (q1, q2, q3) = abs(p1 - q1) + abs(p2 - q2) + abs(p3 - q3)

-- Ejercicio 8
comparar :: Integer -> Integer -> Integer
comparar a b
 | sumaUltimosDosDigitos a < sumaUltimosDosDigitos b = 1
 | sumaUltimosDosDigitos a > sumaUltimosDosDigitos b = (-1)
 | otherwise = 0

sumaUltimosDosDigitos :: Integer -> Integer
sumaUltimosDosDigitos x = (mod x 10) + (mod (div x 10) 10)

-- Ejercicio 9

-- a) funcion que si recibe un 0 te devuelve 1 y si recibe cualquier otro numero te devuelve 0

-- problema f1 (n: R): R {
--     requiere : {True} 
--     asegura : {res = 1 sii n = 0}
--     asegura : {res = 0 sii n /= 0}
-- }


-- b) funcion que si recibe un 1 te devuelve 15 y si recibe -1 te devuelve -15

-- problema f2 (n: R): R {
--     requiere : {True}
--     asegura : {res = 15 sii n = 1}
--     asegura : {res = -15 sii n = -1}
-- }


-- c) funcion que si recibe un numero real menor o igual a 9 te devuelve un 7 y si recibe un numero real mayor
--    a 9 te devuelve un 5 (porque si recibe un nro entre 3 y 9 igual devuelve 7, no llega a la segunda
--    guarda).

-- problema f3 (n: R): R {
--     requiere : {True}
--     asegura : {res = 7 sii n <= 9}
--     asegura : {res = 5 sii n > 9}
-- }


-- d) funcion que recibe dos numeros reales, los suma y luego divide ese resultado por 2

-- problema f4 (x: R, y: R): R {
--     requiere : {True}
--     asegura : {res = (x+y)/2}
-- }


-- e) funcion que recibe una tupla de numeros reales y devuelve la suma de sus elementos dividido por 2

-- problema f5 ((x, y): RxR): R {
--     requiere {True}
--     asegura {res = (x+y)/2}
-- }


-- f) predicado que recibe un numero real y uno entero y redondea el valor del numero real hacia el 0. 
--    Si dicho valor es igual al numero entero el valor es Verdadero, de no ser asi el valor es Falso.

-- pred f6 (x: R, y: Z) {((x >= 0) ^ (⌊x⌋ = y)) V ((x < 0) ^ (⌈x⌉ = y)}