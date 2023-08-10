def getInitial(name,forceUppercase=True):
    if forceUppercase:
        initial=name[0:2].upper()
    else:
        initial=name[0:1]
    return initial

firstName=input('Enter your first name: ')
lastName=input('Enter your last name: ')

firstNameInitial=getInitial(firstName)
lastNameInitial=getInitial(lastName)

print('Your initial is: '+firstNameInitial+' '+lastNameInitial)