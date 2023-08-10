Refactor (add classess/method signatures) from code below to include the following functionality:
1) Users to login/start FileSystem
2) Users to create new directories and store them
3) Users to list/read existing directories (with permissions)
4) Users to create new files in directories and store them
5) Users to list existing files (with permissions)
6) Users to set/edit permissions on files and directories

Rubric:
1. User Interface/API classes/methods
2. Persistance classes/methods
3. Judicious use of SOLID principles

class Permissions:
    _instance = None

    def __new__(cls, read=False, write=False, execute=False):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.read = read
            cls._instance.write = write
            cls._instance.execute = execute
        return cls._instance

    def update_permissions(self, read=False, write=False, execute=False):
        self.read = read
        self.write = write
        self.execute = execute

class User:
    def __init__(self, name):
        self.name = name
        self.groups = set()

    def add_to_group(self, group):
        self.groups.add(group)

class Group:
    def __init__(self, name):
        self.name = name
        self.permissions = Permissions()

class FileSystemElement:
    def __init__(self, name, owner, group):
        self.name = name
        self.owner = owner
        self.group = group

    def access(self, user):
        pass

class File(FileSystemElement):
    def __init__(self, name, content, owner, group):
        super().__init__(name, owner, group)
        self.content = content

    def access(self, user):
        if self.owner.name == user.name or self.group.name in user.groups or self.group.permissions.read:
            print(f"Content of {self.name}: {self.content}")
        else:
            print("You don't have permission to read this file.")

class Directory(FileSystemElement):
    def __init__(self, name, parent=None):
        super().__init__(name, None, None)  # Directories have no owner or group
        self.parent = parent
        self.sub_directories = {}
        self.files = {}

    def add_directory(self, directory_name):
        new_directory = Directory(directory_name, self)
        self.sub_directories[directory_name] = new_directory
        return new_directory

    def add_file(self, file_name, content, owner, group):
        new_file = File(file_name, content, owner, group)
        self.files[file_name] = new_file
        return new_file

    def access(self, user):
        print(f"Accessing directory: {self.name}")

def create_file_system():
    root_directory = Directory("/")
    user1 = User("user1")
    user2 = User("user2")

    # Creating groups and adding users to them
    group1 = Group("group1")
    group2 = Group("group2")
    user1.add_to_group(group1)
    user2.add_to_group(group2)

    # Updating permissions for groups
    group1.permissions.update_permissions(read=True, write=True)
    group2.permissions.update_permissions(read=True, write=False)

    # Creating a file
    root_directory.add_file("file1.txt", "This is the content of file 1", user1, group1)
    root_directory.add_file("file2.txt", "This is the content of file 2", user2, group2)

    # Creating a sub-directory
    sub_directory = root_directory.add_directory("subdir1")
    sub_directory.add_file("file3.txt", "This is the content of file 3", user1, group1)

    return root_directory

# Accessing files and directories via an access path
def access_path(root_directory, path, user):
    current_element = root_directory
    elements = path.strip("/").split("/")
    for element in elements:
        if element in current_element.sub_directories:
            current_element = current_element.sub_directories[element]
        elif element in current_element.files:
            file = current_element.files[element]
            file.access(user)
        else:
            print(f"{element} not found.")

if __name__ == "__main__":
    file_system = create_file_system()

    # Accessing files and directories using access path for user1
    user1 = User("user1")
    access_path(file_system, "/file1.txt", user1)  # Output: Content of file1.txt: This is the content of file 1
    access_path(file_system, "/subdir1/file3.txt", user1)  # Output: Content of file3.txt: This is the content of file 3
    access_path(file_system, "/file2.txt", user1)  # Output: You don't have permission to read this file.
    access_path(file_system, "/non_existent_file.txt", user1)  # Output: non_existent_file.txt not found.

    # Accessing files and directories using access path for user2
    user2 = User("user2")
    access_path(file_system, "/file1.txt", user2)  # Output: Content of file1.txt: This is the content of file 1
    access_path(file_system, "/subdir1/file3.txt", user2)  # Output: You don't have permission to read this file.
    access_path(file_system, "/file2.txt", user2)  # Output: Content of file2.txt: This is the content of file 2
    access_path(file_system, "/non_existent_file.txt", user2)  # Output: non_existent_file.txt not found.
