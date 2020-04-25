gpa=float(input('What is your grade point avarage? '))
lowestGrade=float(input('What was your lowest grade? '))

if gpa >= .85 and lowestGrade>=.70:
    honourRoll=True
else:
    honourRoll=False

if honourRoll:
    print('well done')

