from asmt_6.sql_alchemy import get_session
from file_system_package.models import User  # Import other necessary models

class User:
    def __init__(self, name):
        self.name = name
        self.groups = set()

    def add_to_group(self, group):
        self.groups.add(group)