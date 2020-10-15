def htmlF(tag,text):
    t1='<'
    t2='>'
    t3='/'
    return t1+tag+t2+text+t1+t3+tag+t2
print(htmlF('i','hello'))
