def factorial(n): 
    if n<=0: 
       return 1
    result = 1   
    
    for x in range(1,n+1):
        result = result * x
    return result

for n in range(0,10):
    print(n, factorial(n))