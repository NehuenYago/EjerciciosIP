sumaPrimerosNImparesEspecial :: Integer -> Integer
sumaPrimerosNImparesEspecial n
 | n == 1 = 2 * 1 + 2 
 | mod ((2 * n) - 1) 2 == 0 = sumaPrimerosNImparesEspecial (n - 1)
 | otherwise = (2 * ((2 * n) - 1) + 2) + sumaPrimerosNImparesEspecial (n - 1)


