'''
Using SQLite as the persistance for the directories/files,compile code into a functioning application. 
This application should be executable.The executable should be in Command Line Interface.

Package this application into an archive and submit for review.

Include a short README to instruct how to install this application on machines.

Rubric:
Functioning application

This application should be able to receive a request from a user and respond back with a handle to 
the "root" directory.

Following use cases:
a) User Management : Ability to handle multiple users
b) Ability to create/update/delete directories and files
c) Persistence of directories/files into a database or the local file system
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
    def __init__(self):
        self.root_directory = Directory("/")
        self.logged_in_user = None

    def login_user(self, user):
        self.logged_in_user = user

    def create_directory(self, path, directory_name):
        if not self.logged_in_user:
            print("Please login to the file system before creating a directory.")
            return

        # Check if the user has the necessary permissions to create a directory
        if not self._has_write_permission(path):
            print("You don't have permission to create a directory at the specified path.")
            return

        # Create the new directory and add it to the file system
        directory = Directory(directory_name)
        self._add_to_path(path, directory)

    def list_directory(self, path):
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

    def create_file(self, path, file_name, content):
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
            file = File(file_name, content, self.logged_in_user, directory.group)
            directory.files[file_name] = file
        else:
            print(f"Directory not found at path: {path}")

    def list_files(self, path):
        if not self.logged_in_user:
            print("Please login to the file system before listing files.")
            return

        # Check if the user has the necessary permissions to list files
        if not self._has_read_permission(path):
            print("You don't have permission to list files at the specified path.")
            return

        # List the files in the directory along with their permissions
        directory = self._get_directory(path)
        if directory:
            print(f"Listing files in directory: {path}")
            for name, file in directory.files.items():
                print(f"File: {name}, Permissions: {self._get_permissions(file)}")
        else:
            print(f"Directory not found at path: {path}")

    def set_permissions(self, path, read=False, write=False, execute=False):
        if not self.logged_in_user:
            print("Please login to the file system before setting permissions.")
            return

        # Check if the user has the necessary permissions to set permissions
        if not self._has_write_permission(path):
            print("You don't have permission to set permissions at the specified path.")
            return

        # Set permissions for the file or directory
        element = self._get_element(path)
        if element:
            if isinstance(element, File):
                element.permissions.update_permissions(read=read, write=write, execute=execute)
            else:
                print("Permissions can only be set for files, not directories.")
        else:
            print(f"File or directory not found at path: {path}")

    def _has_write_permission(self, path):
        # Logic to check if the logged-in user has write permission for the specified path
        return True

    def _has_read_permission(self, path):
        # Logic to check if the logged-in user has read permission for the specified path
        return True
    
    def _get_element(self, path):
        current_element = self.root_directory
        elements = path.strip("/").split("/")
        for element in elements:
            if element in current_element.sub_directories:
                current_element = current_element.sub_directories[element]
            elif element in current_element.files:
                current_element = current_element.files[element]
            else:
                return None
        return current_element

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
        # can use the element's owner and group attributes along with the logged-in user to determine permissions
        return f"Read: {element.group.permissions.read}, Write: {element.group.permissions.write}, Execute: {element.group.permissions.execute}"

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
    file_system = FileSystem()

    # Creating groups and adding users to them
    group1 = Group("group1")
    group2 = Group("group2")
    user1 = User("user1")
    user2 = User("user2")
    user1.add_to_group(group1)
    user2.add_to_group(group2)

    # Updating permissions for groups
    group1.permissions.update_permissions(read=True, write=True)
    group2.permissions.update_permissions(read=True, write=False)

    # Login users to the file system
    file_system.login_user(user1)

    # Create new directories
    file_system.create_directory("/", "dir1")
    file_system.create_directory("/dir1", "dir2")
    file_system.create_directory("/dir1", "dir3")

    # Create new files
    file_system.create_file("/dir1", "file1.txt", "This is the content of file 1")
    file_system.create_file("/dir1/dir2", "file2.txt", "This is the content of file 2")

    # Set permissions for directories and files
    file_system.set_permissions("/dir1", read=True, write=False)
    file_system.set_permissions("/dir1/dir2", write=True)

    # List directories and files
    file_system.list_directory("/")
    file_system.list_directory("/dir1")
    file_system.list_files("/dir1")
    file_system.list_files("/dir1/dir2")

    # Access files using access path for user1
    access_path(file_system.root_directory, "/dir1/file1.txt", user1)
    access_path(file_system.root_directory, "/dir1/dir2/file2.txt", user1)

    # Access files using access path for user2
    file_system.login_user(user2)
    access_path(file_system.root_directory, "/dir1/file1.txt", user2)
    access_path(file_system.root_directory, "/dir1/dir2/file2.txt", user2)

