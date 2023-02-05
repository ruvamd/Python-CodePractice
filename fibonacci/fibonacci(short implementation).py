#this is a short and fastest implementation of fibonacci

a,b=0,1
while b<1000:
    print(b,end=' ',flush=True)
    a,b=b,a+b
print()