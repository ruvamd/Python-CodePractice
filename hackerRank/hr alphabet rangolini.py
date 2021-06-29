#alf=['A','B','C','D','E','F','G','H','I','J','K','L','I','M','N','O','Q','R','S','T','U','V','W','X','Y','Z']
# size=input()
# #abcdefghijklmnopqrstuvwxyz
# for i in alf:
#     l=i[0].center('-')
#     print(l)

import string

def print_rangoli():
    alpha = string.ascii_lowercase

    n = int(input())
    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(L[:0:-1]+L))

print_rangoli()