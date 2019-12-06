def getInitial(name,forceUppercase=True):
    if forceUppercase:
        initial=name[0:1].upper()
    else:
        initial=name[0:1]
    return initial
firstName=input('Enter your first name: ')
firstNameInitial=getInitial(firstName)
print('Your initial is: '+firstNameInitial)