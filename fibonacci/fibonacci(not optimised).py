def fibonacci(limit):
    num1=1
    num2=1
    print(num1,end=' ')
    while num2<=limit:
          print(num2,end=' ')
          
          newnum=num1+num2
          num1=num2
          num2=newnum       
    print()
fibonacci(100)