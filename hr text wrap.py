import textwrap

def wrap():
    string=str(input('enter the text: '))
    max_width=int(input('enter the width: '))
    r=textwrap.fill(string,max_width)
    return r

print(wrap())

#-----alt code----
# def wrap(string,max_width):
#     # string=str(input())
#     # max_width=int(input())
#     r=textwrap.fill(string,max_width)
#     return r

# print(wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ',4))

#-----alt code----
# def wrap(string, max_width):
#     string='ABCDEFGHIJKLIMNOQRSTUVWXYZ'
#     max_width=4
#     r=textwrap.fill(string,max_width)
#     return r

# print(wrap('',''))

#-------alt code-----
# import textwrap as tw

# str='ABCDEFGHIJKLIMNOQRSTUVWXYZ'
# width=4

# s=tw.wrap(str,width)
# s=tw.fill(str,width)
# print(s)