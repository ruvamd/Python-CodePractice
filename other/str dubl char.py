'''
Given a string and a non-negative int n, we'll say that the 
front of the string is the first 3 chars, or whatever is there 
if the string is less than length 3. Return n copies of the front;
'''
def front_times(str, n):    
#alternative code    
    #return str[:(3 if len(str)>3 else len(str))]*n

    return str[:3]*n

print(front_times('Chocolate', 2)) #→ 'ChoCho'
print(front_times('Chocolate', 3)) #→ 'ChoChoCho'
print(front_times('Abc', 3)) #→ 'AbcAbcAbc'