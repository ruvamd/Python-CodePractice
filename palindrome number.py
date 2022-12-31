def is_palindrom(x):
    if x<0:
        return False
    else:
        return str(x)==str(x)[::-1]

x=121
print(is_palindrom(x))