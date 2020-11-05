#show first halh of the string
def first_half(str):
    return str[:int(len(str)/2)]
'''
alternative solutions
1.  hs=len(str)/2
    h=int(hs)
    return str[:h]
   
2.  return str[:len(str)/2] 
'''
print(first_half('WooHoo'))
print(first_half('HelloThere'))
print(first_half('abcdef'))
