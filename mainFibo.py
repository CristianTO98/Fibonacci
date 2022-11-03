import time
import timeit

cache = {}
def fibonacci_3(n):
    if n < 2:
        return n
    if n in cache:
        return cache[n]
    res = fibonacci_3(n-1) + fibonacci_3(n-2)
    cache[n] = res
    return res


inicio = time.time()

for i in range(100):
    fibonacci_3(i)
fin = time.time()

print(fin - inicio)
