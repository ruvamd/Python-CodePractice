def main():
    userAge=-99
    while userAge<0 or userAge>120:
         try:userAge=int(input('Enter your age form 0 to 120: '))
         except ValueError:print('Enter number only!')
    print('That is',dogYear(userAge),'in dog years.')

def dogYear(humanYears):
    return humanYears*7
main()