# import re

# def validRomNum(num):
#     pattern=re.compile(r'''^M{0,3}
#                 (CM|CD|D?C{0,3})?
#                 (XC|XL|L?X{0,3})?
#                 (IX|IV|V?I{0,3})?$''',re.VERBOSE)
#     if re.match(pattern,num):
#         return True
#     return False

# print(validRomNum(input('enter the number: ')))

from roman import fromRoman

try:
    print(0 < fromRoman(input('enter the number: ')) < 4000)
except:
    print(False)

# import roman

# # to roman
# number = int(input('> ')) # 10
# print(roman.toRoman(number))

# # from roman
# number = input('> ') # X
# print(roman.fromRoman(number))