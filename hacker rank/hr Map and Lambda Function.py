cube=lambda i:i**3
a,b=0,1
for i in range(5):#int(input())
    print(cube(a),end=' ')
    a,b=b,a+b    

#---alt code---  
cube = lambda x:pow(x,3) # complete the lambda function 
def fibonacci(n):
    # return a list of fibonacci numbers
        lis = [0,1]
        for i in range(2,n):
            lis.append(lis[i-2] + lis[i-1])
        return(lis[0:n])




