def foo(first,second,third,*therest):
    print(f'first: {first}')
    print(f'second: {second}')
    print(f'third: {third}')
    print(f'and all the rest... {(list(therest))}')
foo(1,2,3,4,5)