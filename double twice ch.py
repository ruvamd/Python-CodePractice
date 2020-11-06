#makes double letters in string

def double_char(str):
    return ''.join([c*2 for c in str])
#alternative solution    
    # res=''
    # for x in str:
    #     res+=x*2
    # return res

print(double_char('The'))
print(double_char('AAbb'))
print(double_char('Hi-There'))