def bar(first,second,third,**options):
    if options.get('action')=='sum':
       print('the sum is: %d' %(first+second+third))

    if options.get('number')=='first':
        return first

result=bar(1,2,3, action='sum',number='first')
print('result: %d' %(result))

    