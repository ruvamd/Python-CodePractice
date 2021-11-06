x=''
with open('UW/python crash cource/chapter 10/programming_poll.txt','a') as f:

    while x!='q':
        x=input('why do you like programming?:')
        # for line in x:
        f.write(f'{x}\n')