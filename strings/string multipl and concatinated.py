def strF(str):
    if len(str)<=3:
        return str*3
    return str[0:3]*3
print(strF('hello'))