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

class Admin(User):
    def __init__(self,first_name,last_name,age,location):
        super().__init__(first_name,last_name,age,location)
        self.privileges=['can add post','can delete post','can update post']
    
    def show_privileges(self):
        print(f'the admin privileges are {self.privileges}')

class Privileges:
    def __init__(self,privileges=['can add post','can delete post','can update post']):
        self.privileges=privileges
    
    def show_privileges(self):
        print(f'the admin privileges are {self.privileges}')