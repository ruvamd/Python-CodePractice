from asmt_6.sql_alchemy import get_session

class UserClass:
    def __init__(self, name):
        self.name = name
        self.groups = set()

    def add_to_group(self, group):
        self.groups.add(group)

User = UserClass  # Assign the class to the name 'User' to maintain compatibility

