'''
input:
..12345678910111213141516171820212223
'''
import re
s=re.match(r'.*(\w)\1','..12345678910111213141516171820212223')
if s.group(1):
    print(1)
else: print(-1)

#---alt code---
# S='..12345678910111213141516171820212223'
# m=re.match(r'.*?([a-z0-9A-Z])\1', S)
# if m is None:
#     print(str(-1))
# else:
#     print(m.group(1))
'''
output: 
1
else output -1 if not alphanumeric character
'''