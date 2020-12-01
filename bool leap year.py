def is_leap(year):

#alternative code works,except one test
    # leap=True
    # notLeap=False
    
    # if year%4==0:
    #     return leap
    # elif year%100!=0:
    #     return notLeap
    # else: year%400==0
    # return leap

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


year = int(input('enter the year: '))
print(is_leap(year))

