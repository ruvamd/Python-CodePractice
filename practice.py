x=-123
def rev(x):
    if x>=0:
        result=int(str(x)[::-1])
    else: 
        result=-int(str(-x)[::-1]) 
    return result if abs(result)<2**31-1 else 0
print(rev(x))