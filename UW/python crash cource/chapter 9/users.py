class User:
    def __init__(self,first_name,last_name,age,location):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.location=location

    def describe_user(self):
        print(f'the user name {self.first_name} {self.last_name} with age of {self.age} lives in {self.location}')
        # print(f'the user name is {self.first_name}.')
        # print(f'the user last name is {self.last_name}.')
        # print(f'the users age is {self.age}.')
        # print(f'the user location is {self.location}.')
    
    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}.')

vadim=User('vadim','rusu',38,'seattle')
colea=User('colea','julif',38,'colosovo')

vadim.describe_user()
vadim.greet_user()

colea.describe_user()
colea.greet_user()

