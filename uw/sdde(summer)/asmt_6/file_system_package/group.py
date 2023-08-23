from .permissions import Permissions

from asmt_6.sql_alchemy import get_session
from file_system_package.models import Group  # Import other necessary models

class Group:
    def __init__(self, name):
        self.name = name
        self.permissions = Permissions()
