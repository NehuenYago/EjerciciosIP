prod :: Integer -> Integer
prod 1 = ((2 * 1) ^ (2 :: Integer) + 2 * (2 * 1)) * 3
prod n = (((2 * n) ^ (2 :: Integer)) + 2 * (2 * n)) * ((((2 * n) - 1) ^ (2 :: Integer)) + 2 * ((2 * n) - 1)) * prod (n - 1)
