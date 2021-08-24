'''
input:
4
4.0O0
-1.00
+4.54
SomeRandomStuff
'''
import re
#+,-,. valid
#at least one decimal ex:12.0
x=[]
for i in range(int(input())):#t-the number of test cases
    i=bool(re.match(r'[-+]?\d*\.\d+$',input()))
    x.append(i)
print(*x,sep='\n')

# #(r'^[-+]?[0-9]*\.[0-9]+$'

# for _ in range(int(input())):
# 	print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$',input())))
'''
output:
False
True
True
False
'''