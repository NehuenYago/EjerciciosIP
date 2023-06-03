def fibonacciNoRecursivo(n: int) -> int:
    fibonacci:int
    fib0:int = 0
    fib1:int = 1

    if n == 0:
        return fib0
    if n == 1:
        return fib1
    while n > 1:
        fibonacci = fib0 + fib1
        fib0 = fib1
        fib1 = fibonacci
        n -= 1
    return fibonacci
