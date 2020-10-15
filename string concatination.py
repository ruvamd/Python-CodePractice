def strFunc(str):
    a='not '
    if len(str[0:3])>=3 and str[0:3]=='not':
        return str
    return a+str
print(strFunc('not hello'))