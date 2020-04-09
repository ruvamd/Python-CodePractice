def foo(a,b,c,*args):
    return len(args)
def bar(a,b,c,**kwargs):
    return kwargs['magicnumber']==7

if foo(1,2,3,4)==1:
    print('good.')
if foo(1,2,3,4,5)==2:
    print('better.')

if bar(1,2,3,magicnumber=6)==False:
    print('great.')
if bar(1,2,3,magicnumber=7)==True:
    print('awesome!')
