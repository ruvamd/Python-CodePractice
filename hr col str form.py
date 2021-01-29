def print_formatted():
    n=list(range(1,int(input())+1))
    for i in n:
        d=str(i).rjust(2,' ')
        o=oct(i).replace('0o','').rjust(2,' ')
        h=hex(i).replace('0x','').upper().rjust(2,' ')
        b=bin(i).replace('0b','').rjust(2,' ')
        print(d,o,h,b)

print_formatted()

#----alt code------
#def print_formatted(number):
    # l=len(('{0:b}').format(number))
    # for i in range(1,number+1):
    #     print('{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}'.format(i,w=l))