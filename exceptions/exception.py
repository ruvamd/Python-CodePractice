actor={'name':'jone jones','rank':'good'}

def getLastName():
    return actor['name'].split()[1]
getLastName()

def getRank():
    return actor['rank'].split()[0]
getRank()

print('secection done')
print(f'tha actors last name is: {getLastName()} and rank is: {getRank()}')
