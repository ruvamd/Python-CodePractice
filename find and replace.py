userName='name*lastname'
position=userName.find('lastname')

if position>-1:
    print('user name contains lastname')

userName=userName.replace('me*',' ')
print(userName)

