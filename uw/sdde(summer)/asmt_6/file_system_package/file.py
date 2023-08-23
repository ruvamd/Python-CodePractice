from .file_system_element import FileSystemElement

class File(FileSystemElement):
    def __init__(self, name, content, owner, group):
        super().__init__(name, owner, group)
        self.content = content

    def access(self, user):
        if self.owner.name == user.name or self.group.name in user.groups or self.group.permissions.read:
            print(f"Content of {self.name}: {self.content}")
        else:
            print("You don't have permission to read this file.")