'''
Given two strings, return True if either of the strings appears at 
the very end of the other string, ignoring upper/lower case 
differences (in other words, the computation should not 
be "case sensitive"). Note: s.lower() returns the lowercase 
version of a string.
'''
import re
def end_other(a, b):
    long_s, short_s = (a,b) if len(a) >= len(b) else (b,a)
    return long_s.lower().endswith(short_s.lower())

print(end_other('Hiabc', 'abc')) #→ True
print(end_other('AbC', 'HiaBc')) #→ True
print(end_other('abc', 'abXabc')) #→ True
print(end_other('Hiabc', 'abcd')) #→ False