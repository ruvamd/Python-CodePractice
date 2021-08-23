'''
2
9587456281
1252478965
'''
import re
number=int(input())
numbers = [input() for _ in range(number)]
pattern = re.compile(r'^[7-9]\d{9}$')
for num in numbers:
    if pattern.match(num):
        print('Yes')
    else: print('No')
'''
YES
NO
'''

