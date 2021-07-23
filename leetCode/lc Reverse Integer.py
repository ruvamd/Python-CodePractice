'''
class Solution:
    def reverse(self, x):
        res=int(str(x)[::-1]) if x > -1 else int(str(abs(x))[::-1])*-1
        if res < -(2**31) or res > (2**31)-1: return 0
        return res
'''
x = -720

def reverse(x):
    if x>=0:
        r=int(str(x)[::-1])   
    else:
        r=-int(str(-x)[::-1])
    return r if abs(r)<2**31-1 else 0

print(reverse(x))
'''
def reverse_signed(num):
    sum=0
    sign=1
    if num<0: #make num positive
        sign=-1
        num=num*-1 
    while num>0:
        rem=num%10
        sum=sum*10+rem
        num=num//10
    if not -2147483648<sum<2147483647:
        return 0
    return sign*sum

print(reverse_signed(-123))
'''
