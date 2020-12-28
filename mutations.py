def mutate_string(string,position,character):
    return string[:position]+character+string[position+1:]
print(mutate_string('abracadabra',5,'k'))


#alt code 0
# def mutate_string(string):
#     s=list('abracadabra')
#     p=int(5)
#     c='k'
#     s[p]=c
#     s=''.join(s)
#     return(s)
# print(mutate_string(''))

#alt code 1
# s=list('abracadabra')
# p=int(5)
# c='k'
# s[p]=c
# s=''.join(s)
# print(s)

#alt code 2
# s=list(input('enter the string: '))
# p=int(input('enter the position: '))
# c=input('enter the character: ')
# s[p]=c
# s=''.join(s)
# print(s)


