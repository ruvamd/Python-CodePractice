class User:
    def __init__(self,first_name,last_name,age,location):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.location=location

    def describe_user(self):
        print(f'the user name {self.first_name} {self.last_name} with age of {self.age} lives in {self.location}')

class Admin(User):
    def __init__(self,first_name,last_name,age,location):
        super().__init__(first_name,last_name,age,location)
        self.privileges=['can add post','can delete post','can update post']
    
    def show_privileges(self):
        print(f'the admin privileges are {self.privileges}')

call_admin=Admin('vadim','rusu',38,'seattle')
call_admin.show_privileges()