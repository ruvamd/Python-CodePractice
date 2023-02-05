def fibonacci(n, cache={}):
    if n <= 1:
        return n
    if n not in cache:
        cache[n] = fibonacci(n-1, cache) + fibonacci(n-2, cache)
    return cache[n]


for i in range(0, 10):
    print(fibonacci(i))
