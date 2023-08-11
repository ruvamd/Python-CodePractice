class FileSystemElement:
    def __init__(self, name, owner, group):
        self.name = name
        self.owner = owner
        self.group = group

    def access(self, user):
        pass