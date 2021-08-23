import re
'''
input:
2  
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>
'''
N = int(input())

for i in range(N):
    name, email = input().split()
    pattern="<[a-z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>"
    if bool(re.match(pattern, email)):
        print(name,email)
'''
output:
DEXTER <dexter@hotmail.com>
'''