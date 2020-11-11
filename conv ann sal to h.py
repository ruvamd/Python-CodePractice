yearSal=int(input('Enter the year salary: '))
def convYearToHourSal():
    return round(yearSal/12/4/5/8,2)

print(f'The annual ${yearSal} salary in the hour is: {convYearToHourSal()}')

