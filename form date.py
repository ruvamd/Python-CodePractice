from datetime import datetime
birthday=input('when is your birthday: (dd/mm/yyyy)? ')
birthdayDate=datetime.strptime(birthday,'%d/%m/%Y')
print('birthdate: '+str(birthdayDate))