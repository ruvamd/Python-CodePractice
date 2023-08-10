def main():
    kitten('meaw','grrr','purr')
def kitten(*args):
    if len(args):
        for s in args:
            print(s)
    else: print('meaw')
main()  
