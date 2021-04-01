'''
input: 100,000,000.000
output: 
100
000
000
000
'''
import re

rx=re.split(r'\D',input())
for i in rx:
    print(i)

