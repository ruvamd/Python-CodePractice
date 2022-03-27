def make_posh(func):
    def wrapper():
        print('+---------+')
        print('|         |')
        result=func()
        print(result)
        print('|         |')
        print('+=========+')
        return(result)
    return wrapper

@make_posh
def pfib():
    '''Print out Fibonacci'''
    return ' Fibonacci '

pfib()

# pfib=make_posh(pfib)
# print(pfib())