from .permissions import Permissions

class Group:
    def __init__(self, name):
        self.name = name
        self.permissions = Permissions()
