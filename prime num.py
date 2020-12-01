#check alternatives

def solution(i):
    p=gPn()
    return p[i:i+5]
    
def gPn():
    s=''
    pr=2
    while len(s)<10005:
        s+=str(pr)
        pr+=1
        while not is_prime(pr):
            pr+=1
    return s
    
def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

print(solution(0))
print(solution(3))