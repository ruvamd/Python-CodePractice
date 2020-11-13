'''
Return the number of times that the string "hi" appears 
anywhere in the given string.
'''
def count_hi(str):
    return str.count('hi')

print(count_hi('abc hi ho')) #→ 1
print(count_hi('ABChi hi')) #→ 2
print(count_hi('hihi')) #→ 2