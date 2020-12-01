def main():
    for i in inclusiveRange(5,25,5):
        print(i,end=' ')
    print()
def inclusiveRange(*args):
    numargs=len(args)
    start=0
    step=1

    if numargs<1:
        raise TypeError(f'expected at least 1 argument,got {numargs}')
    elif numargs==1:stop=args[0]
    elif numargs==2:(start,stop)=args
    elif numargs==3:(start,stop,step)=args
    else:raise TypeError(f'expected at most 3 arguments,got {numargs}')
    i=start
    while i<=stop:
        yield i
        i+=step
main()
