-- Ejercicio 1
fibonacci :: Integer -> Integer
fibonacci n
 | n == 0 = 0
 | n == 1 = 1
 | otherwise = fibonacci (n - 1) + fibonacci (n - 2)

-- con Pattern Matching
fibonacciPM :: Integer -> Integer
fibonacciPM 0 = 0
fibonacciPM 1 = 1
fibonacciPM n = fibonacciPM (n - 1) + fibonacciPM (n - 2)

-- Ejercicio 2
parteEntera :: Float -> Integer
parteEntera x
 | x < 1 = 0
 | otherwise = 1 + parteEntera (x - 1)

-- Ejercico 3
esDivisible :: Integer -> Integer -> Bool
esDivisible x y
 | (x - y) == 0 = True
 | (x - y) < 0 = False
 | otherwise = esDivisible (x - y) y

-- Ejercicio 4
sumaImpares :: Integer -> Integer
sumaImpares 1 = 1
sumaImpares n = 2 + sumaImpares (n - 1)

-- Ejercicio 5
medioFact :: Integer -> Integer
medioFact 0 = 1
medioFact 1 = 1
medioFact n = n * medioFact (n - 2)

-- Ejercicio 6
sumaDigitos :: Integer -> Integer
sumaDigitos 0 = 0
sumaDigitos n = mod n 10 + sumaDigitos (div n 10)

-- Ejercicio 7
todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n
 | n < 10 = True
 | mod n 10 == mod (div n 10) 10 = True && todosDigitosIguales (div n 10)
 | otherwise = False

-- Ejercicio 8
iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i = mod (div n (10 ^ (cantDigitos n - i))) 10

cantDigitos :: Integer -> Integer
cantDigitos n
 | n < 10 = 1
 | otherwise = 1 + cantDigitos (div n 10)

-- Ejercicio 9
esCapicua :: Integer -> Bool
esCapicua n
 | n < 10 = True
 | mod n 10 == div n (10 ^ (cantDigitos n - 1)) = True && esCapicua (div (mod n (10 ^ (cantDigitos n - 1))) 10)
 | otherwise = False

-- Ejercicio 10
-- a)
f1 :: Integer -> Integer
f1 0 = 1
f1 n = 2 ^ n + f1 (n - 1)

-- b)
f2 :: Integer -> Float -> Float
f2 1 q = q
f2 n q = q ^ n + f2 (n - 1) q

-- c)
f3 :: Integer -> Float -> Float
f3 1 q = q ^ 2 + q
f3 n q = q ^ (2 * n) + q ^ ((2 * n) - 1) + f3 (n - 1) q

-- d)
-- f4 calcula la sumatoria de q^i de n a 2n
f4 :: Integer -> Float -> Float
f4 0 q = 1
f4 n q = (f4A n q) - (f4B n q)

-- f4A calcula la sumatoria de q^i de 0 a 2n
f4A :: Integer -> Float -> Float
f4A 0 q = 1
f4A n q = q ^ (2 * n) + q ^ ((2 * n) - 1) + f4A (n - 1) q

-- f4B calcula la sumatoria de q^i de 0 a n-1. tiene 2 caso base para que n - 2 nunca pueda "saltar" el caso base n=0 y se vaya al negativo
f4B :: Integer -> Float -> Float
f4B 0 q = 1
f4B 1 q = q + 1
f4B n q = q ^ (n - 1) + f4B (n - 2) q 

-- Ejercicio 11
-- a)
eAprox :: Integer -> Float
eAprox 0 = 1
eAprox n =  (1.0 / fromIntegral (factorial n)) + eAprox (n - 1)

factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n - 1)

-- b)
e :: Float
e = eAprox 10

-- Ejercicio 12
raizDe2Aprox :: Integer -> Float
raizDe2Aprox n = (sucesion n) - 1

sucesion :: Integer -> Float
sucesion 1 = 2
sucesion n = 2 + (1 / (sucesion (n - 1)))

-- Ejercicio 13
sumatoriaNM :: Integer -> Integer -> Integer
sumatoriaNM 1 m = sumatoriaM 1 m
sumatoriaNM n m = sumatoriaM n m + sumatoriaNM (n - 1) m

sumatoriaM :: Integer -> Integer -> Integer
sumatoriaM n 1 = n
sumatoriaM n m = (n ^ m) + sumatoriaM n (m - 1)

-- Ejercicio 14
sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias q n 1 = recursionEnN q n 1
sumaPotencias q n m = recursionEnN q n m + sumaPotencias q n (m - 1)

recursionEnN :: Integer -> Integer -> Integer -> Integer
recursionEnN q 1 m = q ^ (1 + m)
recursionEnN q n m = q ^ (n + m) + recursionEnN q (n - 1) m

-- Ejercicio 15
sumaRacionales :: Integer -> Integer -> Float
sumaRacionales 1 m = sumaRacionalesAux 1 m
sumaRacionales n m = sumaRacionalesAux n m + sumaRacionales (n - 1) m

sumaRacionalesAux :: Integer -> Integer -> Float
sumaRacionalesAux n 1 = fromInteger n
sumaRacionalesAux n m = ((fromIntegral n) / (fromInteger m)) + sumaRacionalesAux n (m - 1)

-- Ejercicio 16
-- a)
menorDivisor :: Integer -> Integer
menorDivisor 1 = 1
menorDivisor n = menorDivisorAux n 2

menorDivisorAux :: Integer -> Integer -> Integer
menorDivisorAux n m
 | mod n m == 0 = m
 | otherwise = menorDivisorAux n (m + 1)

--  b)
esPrimo :: Integer -> Bool
esPrimo n
 | n /= 1 && (menorDivisor n == n) = True
 | otherwise = False

-- c)
sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos n m = comparaDivisores n m 2

comparaDivisores :: Integer -> Integer -> Integer -> Bool
comparaDivisores n m i
 | (i > n) || (i > m) = True
 | (mod n i == 0) && (mod m i == 0) = False
 | otherwise = comparaDivisores n m (i + 1)

-- --  d)
nEsimoPrimo :: Integer -> Integer
nEsimoPrimo n = nEsimoPrimoAux n 2 

nEsimoPrimoAux :: Integer -> Integer -> Integer
nEsimoPrimoAux n i
 | esPrimo i && n == 1 = i
 | esPrimo i = nEsimoPrimoAux (n - 1) (i + 1)
 | otherwise = nEsimoPrimoAux n (i + 1)

-- Ejercicio 17
esFibonacci :: Integer -> Bool
esFibonacci n = esFibonacciAux n 0

esFibonacciAux :: Integer -> Integer -> Bool
esFibonacciAux n i
 | fibonacci i < n = esFibonacciAux n (i + 1)
 | fibonacci i == n = True
 | otherwise = False

-- Ejercicio 18
mayorDigitoPar :: Integer -> Integer
mayorDigitoPar n = mayorDigitoParAux n (-1)

mayorDigitoParAux :: Integer -> Integer -> Integer
mayorDigitoParAux n m 
 | n < 10 && devuelvePar n >= m = devuelvePar n
 | n < 10 && devuelvePar n < m = m
 | devuelvePar (ultimoDigito n) >= m = mayorDigitoParAux (div n 10) (devuelvePar (ultimoDigito n))
 | devuelvePar (ultimoDigito n) < m = mayorDigitoParAux (div n 10) m

devuelvePar :: Integer -> Integer
devuelvePar n
 | (mod n 2) == 0 = n
 | otherwise = (-1)

ultimoDigito :: Integer -> Integer
ultimoDigito n = mod n 10

-- Ejercicio 19
esSumaInicialDePrimos :: Integer -> Bool
esSumaInicialDePrimos n = esSumaInicialDePrimosAux n 1

esSumaInicialDePrimosAux :: Integer -> Integer -> Bool
esSumaInicialDePrimosAux n i
 | n == contadorPrimos i = True
 | n > contadorPrimos i = esSumaInicialDePrimosAux n (i + 1)
 | otherwise = False 

contadorPrimos :: Integer -> Integer
contadorPrimos 1 = nEsimoPrimo 1
contadorPrimos i = nEsimoPrimo i + contadorPrimos (i - 1)

-- Ejercicio 20
tomaValorMax :: Integer -> Integer -> Integer
tomaValorMax n1 n2 = tomaValorMaxAux n1 (n1 + 1) n2

tomaValorMaxAux :: Integer -> Integer -> Integer -> Integer
tomaValorMaxAux n1 i n2
 | i > n2 = n1
 | sumaDivisores n1 >= sumaDivisores i = tomaValorMaxAux n1 (i + 1) n2
 | otherwise = tomaValorMaxAux i (i + 1) n2

sumaDivisores :: Integer -> Integer
sumaDivisores n = sumaDivisoresAux n 1

sumaDivisoresAux :: Integer -> Integer -> Integer
sumaDivisoresAux n i
 | n == i = i
 | mod n i == 0 = i + sumaDivisoresAux n (i + 1)
 | otherwise = sumaDivisoresAux n (i + 1)