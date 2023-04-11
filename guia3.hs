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
