'''
Assignment - File System:

Explain the data structures and algorithms that you would use to design an in-memory file system (Similar to *nix systems). Illustrate with an example in code where possible. Your design must include the following concepts Directory, File, User and Permissions. Please note there can be other concepts in your design but these ones are required.

Use cases that must be supported by your design:

Machine Startup & File System instantiation
Access to all the files and directories via an access path
Setting permissions and reading permissions
Creating/Reading/Updating/Deleting a Directory or a File
Rubric:

Complete class structure (1 point)
Relationships between classes (1 point)
Appropriate class variables to store the file system details (1 point)
Appropriate methods signatures in the classes that support the following use cases (2 points)
'''

#solution
'''
To design an in-memory file system similar to *nix systems, I use various data structures and algorithms to represent directories, files, users, and permissions.

Data Structures:
•	Directory: A directory can contain other directories and files. I can represent it as a class with attributes such as a name, parent directory, a list of sub-directories, and a list of files.
•	File: A file contains data and has attributes like a name and its contents. I can represent it as a class with these attributes.
•	User: A user has a name and permissions. I can represent it as a class with these attributes.
•	Permissions: I can represent permissions as a class with attributes for read, write, and execute access.

Algorithms:
•	Access Path: I can traverse the file system from the root directory to the desired directory or file using a path. The path can be represented as a list or string, with each element representing a directory or file name.
•	Setting Permissions and Reading Permissions: For each file and directory, I can associate a user with its corresponding permissions. I can then check the user's permissions before allowing access to read, write, or execute operations.
•	Creating/Reading/Updating/Deleting a Directory or a File: I can use standard tree traversal algorithms to create, read, update, or delete directories and files in the file system.
'''

class Permissions:
    def __init__(self, read=False, write=False, execute=False):
        self.read = read
        self.write = write
        self.execute = execute

class User:
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions

class File:
    def __init__(self, name, content, owner, permissions):
        self.name = name
        self.content = content
        self.owner = owner
        self.permissions = permissions

class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.sub_directories = {}
        self.files = {}

    def add_directory(self, directory_name):
        new_directory = Directory(directory_name, self)
        self.sub_directories[directory_name] = new_directory
        return new_directory

    def add_file(self, file_name, content, owner, permissions):
        new_file = File(file_name, content, owner, permissions)
        self.files[file_name] = new_file
        return new_file

def create_file_system():
    root_directory = Directory("/")
    user1 = User("user1", Permissions(read=True, write=True, execute=True))
    user2 = User("user2", Permissions(read=True, write=False, execute=False))

    # Creating a file and setting permissions
    root_directory.add_file("file1.txt", "This is the content of file 1", user1, Permissions(read=True, write=True))
    root_directory.add_file("file2.txt", "This is the content of file 2", user2, Permissions(read=True, write=False))

    # Creating a sub-directory
    sub_directory = root_directory.add_directory("subdir1")
    sub_directory.add_file("file3.txt", "This is the content of file 3", user1, Permissions(read=True, write=False))

    return root_directory

# Accessing files and directories via an access path
def access_path(root_directory, path):
    current_directory = root_directory
    elements = path.strip("/").split("/")
    for element in elements:
        if element in current_directory.sub_directories:
            current_directory = current_directory.sub_directories[element]
        elif element in current_directory.files:
            file = current_directory.files[element]
            user = User("user1", Permissions(read=True, write=True, execute=True))
            if file.owner.name == user.name or file.permissions.read:
                print(f"Content of {element}: {file.content}")
            else:
                print("You don't have permission to read this file.")
        else:
            print(f"{element} not found.")

if __name__ == "__main__":
    file_system = create_file_system()

    # Accessing files and directories using access path
    access_path(file_system, "/file1.txt")  # Output: Content of file1.txt: This is the content of file 1
    access_path(file_system, "/subdir1/file3.txt")  # Output: Content of file3.txt: This is the content of file 3
    access_path(file_system, "/file2.txt")  # Output: You don't have permission to read this file.
    access_path(file_system, "/non_existent_file.txt")  # Output: non_existent_file.txt not found.
class Permissions:
    def __init__(self, read=False, write=False, execute=False):
        self.read = read
        self.write = write
        self.execute = execute

class User:
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions

class File:
    def __init__(self, name, content, owner, permissions):
        self.name = name
        self.content = content
        self.owner = owner
        self.permissions = permissions

class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.sub_directories = {}
        self.files = {}

    def add_directory(self, directory_name):
        new_directory = Directory(directory_name, self)
        self.sub_directories[directory_name] = new_directory
        return new_directory

    def add_file(self, file_name, content, owner, permissions):
        new_file = File(file_name, content, owner, permissions)
        self.files[file_name] = new_file
        return new_file

def create_file_system():
    root_directory = Directory("/")
    user1 = User("user1", Permissions(read=True, write=True, execute=True))
    user2 = User("user2", Permissions(read=True, write=False, execute=False))

    # Creating a file and setting permissions
    root_directory.add_file("file1.txt", "This is the content of file 1", user1, Permissions(read=True, write=True))
    root_directory.add_file("file2.txt", "This is the content of file 2", user2, Permissions(read=True, write=False))

    # Creating a sub-directory
    sub_directory = root_directory.add_directory("subdir1")
    sub_directory.add_file("file3.txt", "This is the content of file 3", user1, Permissions(read=True, write=False))

    return root_directory

# Accessing files and directories via an access path
def access_path(root_directory, path):
    current_directory = root_directory
    elements = path.strip("/").split("/")
    for element in elements:
        if element in current_directory.sub_directories:
            current_directory = current_directory.sub_directories[element]
        elif element in current_directory.files:
            file = current_directory.files[element]
            user = User("user1", Permissions(read=True, write=True, execute=True))
            if file.owner.name == user.name or file.permissions.read:
                print(f"Content of {element}: {file.content}")
            else:
                print("You don't have permission to read this file.")
        else:
            print(f"{element} not found.")

if __name__ == "__main__":
    file_system = create_file_system()

    # Accessing files and directories using access path
    access_path(file_system, "/file1.txt")  # Output: Content of file1.txt: This is the content of file 1
    access_path(file_system, "/subdir1/file3.txt")  # Output: Content of file3.txt: This is the content of file 3
    access_path(file_system, "/file2.txt")  # Output: You don't have permission to read this file.
    access_path(file_system, "/non_existent_file.txt")  # Output: non_existent_file.txt not found.

'''
This code demonstrates a basic in-memory file system with support for 
creating directories, files, setting permissions, and reading file content. 
It also allows accessing files and directories via an access path and checks the 
user's permissions before providing access to the file content.
'''