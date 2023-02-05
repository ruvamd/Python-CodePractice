cache={0:0,1:1}

def fib(n): # base case
    if n in cache:
        return cache[n]
    cache[n]=fib(n-1)+fib(n-2)
    return cache[n]

for i in range(0,10): # recursive case
    print(fib(i))
