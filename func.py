def getInitial(name):
    initial=name[0:1].upper()
    return initial

firstName=input('Enter your first name: ')
firstNameInitial=getInitial(firstName)

lastName=input('Enter your last name: ')
lastNameInitial=getInitial(lastName)

print('Your initial are: '+firstNameInitial+lastNameInitial)