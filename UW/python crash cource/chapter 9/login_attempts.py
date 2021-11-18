class User:
    def __init__(self,first_name,last_name,age,location):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.location=location
        self.login_attempt=0

    def describe_user(self):
        # print(f'the user name {self.first_name} {self.last_name} with age of {self.age} lives in {self.location}')
        print(f'{self.login_attempt}')
    def increment_login_attempt(self,attempt):
        self.login_attempt+=attempt
        
    def reset_login_attempt(self,reset):
        self.login_attempt-=reset

user=User('vadim','rusu',38,'seattle')
user.increment_login_attempt(1)
user.increment_login_attempt(1)
user.increment_login_attempt(1)

user.reset_login_attempt(1)
user.reset_login_attempt(1)
user.describe_user()

