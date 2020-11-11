def getInitial(name):
    initial=name[0:1].upper()
    return initial

firstName=input('Enter your first name: ')
lastName=input('Enter your last name: ')

print('Your initials are: '+getInitial(firstName)+getInitial(lastName))