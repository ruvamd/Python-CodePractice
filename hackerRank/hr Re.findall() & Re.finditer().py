'''
Task
given a string S. It consists of alphanumeric characters, spaces and symbols(+,-).
find all the substrings of S that contains 2 or more vowels.
Also, these substrings must lie in between  consonants and should contain vowels only.
'''
import re

# S='rabcdeefgyYhFjkIoomnpOeorteeeeet' #alphanumeric characters, spaces and symbols(+,-)
# subStr=re.findall('(ee)()',text)
# subStr=re.findall('[aeiouAEIOU]{2,}',S)#\n
# print('\n'.join(subStr or -1))

# if subStr:
#     for i in subStr:
#         print(i)
# else: print(-1)

v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), input('enter text: ' ), flags = re.I)
print('\n'.join(m or ['-1']))
