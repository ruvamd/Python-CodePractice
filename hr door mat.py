# # cen_text='WELCOME'

# # char=|.-
# n=7
# m=n*3
# #mat_size=(n*m)

# vert_line='|'
# dot='.'
# line='-'

# for i in range(n):
#     print(dot.rjust(n,line)+vert_line+dot.ljust(n,line))

#-----alt code-----
# height, length = map(int, input().split())

# for i in range(0,height//2):
#     s = '.|.' * (i * 2 + 1)
#     print(s.center(length,'-'))
# print('WELCOME'.center(length, '-'))

# for i in range(height//2-1,-1,-1):
#     s = '.|.' * (i * 2 + 1)
#     print(s.center(length,'-'))

N, M = map(int, input('enter high&width(exm.7 27): ').split(" "))

for i in range(N):
    pattern = ".|."
    if i < (N-1)/2:
            print((pattern * (2*i+1)).center(M, "-"))
    elif i == (N-1)/2:
        print("WELCOME".center(M, "-"))
    else:
        print((pattern * (2*(N-1-i)+1)).center(M, "-"))