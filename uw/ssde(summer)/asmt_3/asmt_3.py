'''
add classess/method signatures to the code below to allow:
1) Users to login/start FileSystem
2) Users to create new directories and store them
3) Users to list/read existing directories (with permissions)
4) Users to create new files in directories and store them
5) Users to list existing files (with permissions)
6) Users to set/edit permissions on files and directories

specify what parts of code are using the objects that have already defined.
'''

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

class FileSystem:
    def __init__(self, root_directory):
        self.root_directory = root_directory
        self.logged_in_user = None

    def login_user(self, user):
        self.logged_in_user = user

    def create_directory(self, path, directory_name, owner, group):
        if not self.logged_in_user:
            print("Please login to the file system before creating a directory.")
            return

        # Check if the user has the necessary permissions to create a directory
        if not self._has_write_permission(path):
            print("You don't have permission to create a directory at the specified path.")
            return

        # Create the new directory and add it to the file system
        directory = Directory(directory_name, self.root_directory)
        self._add_to_path(path, directory)
        directory.owner = owner
        directory.group = group

    def _has_write_permission(self, path):
        # Logic to check if the logged-in user has write permission for the specified path
        return True  # Replace this with your actual permission-checking logic

    def _add_to_path(self, path, directory):
        current_element = self.root_directory
        elements = path.strip("/").split("/")
        for element in elements:
            if element in current_element.sub_directories:
                current_element = current_element.sub_directories[element]
            else:
                print(f"{element} not found.")
                return

        current_element.sub_directories[directory.name] = directory

    def list_directory(self, path, user):
        if not self.logged_in_user:
            print("Please login to the file system before listing a directory.")
            return

        # Check if the user has the necessary permissions to list the directory
        if not self._has_read_permission(path):
            print("You don't have permission to list the directory at the specified path.")
            return

        # List the contents of the directory
        directory = self._get_directory(path)
        if directory:
            print(f"Listing contents of directory: {path}")
            for name, element in directory.sub_directories.items():
                print(f"Directory: {name}, Permissions: {self._get_permissions(element)}")

            for name, file in directory.files.items():
                print(f"File: {name}, Permissions: {self._get_permissions(file)}")
        else:
            print(f"Directory not found at path: {path}")

    def _has_read_permission(self, path):
        # Logic to check if the logged-in user has read permission for the specified path
        return True  # Replace this with your actual permission-checking logic

    def create_file(self, path, file_name, content, owner, group):
        if not self.logged_in_user:
            print("Please login to the file system before creating a file.")
            return

        # Check if the user has the necessary permissions to create a file
        if not self._has_write_permission(path):
            print("You don't have permission to create a file at the specified path.")
            return

        # Create the new file and add it to the specified directory
        directory = self._get_directory(path)
        if directory:
            file = File(file_name, content, owner, group)
            directory.files[file_name] = file
        else:
            print(f"Directory not found at path: {path}")

    def _has_write_permission(self, path):
        # Logic to check if the logged-in user has write permission for the specified path
        return True  # Replace this with your actual permission-checking logic

    def _get_directory(self, path):
        current_element = self.root_directory
        elements = path.strip("/").split("/")
        for element in elements:
            if element in current_element.sub_directories:
                current_element = current_element.sub_directories[element]
            else:
                return None

        return current_element

    def _get_permissions(self, element):
        # Logic to get permissions for an element (file or directory)
        # You can use the element's owner and group attributes along with the logged-in user to determine permissions
        return "Read: True, Write: True, Execute: False"  # Replace this with your actual permissions representation

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
def access_path(file_system, path, user):
    file_system.login_user(user)  # Login the user to the file system
    current_element = file_system.root_directory
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
    file_system = FileSystem(create_file_system())

    # Accessing files and directories using access path for user1
    user1 = User("user1")
    file_system.login_user(user1)

    # List directories with permissions
    file_system.list_directory("/", user1)  # List the root directory

    # Create new files in directories
    file_system.create_file("/", "file1.txt", "This is the content of file 1", user1, user1)  # Create a new file at the root
    file_system.create_file("/subdir1", "file2.txt", "This is the content of file 2", user1, user1)  # Create a new file inside a directory
