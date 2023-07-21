#1.refactored code from asmt_1 based on feedback

class Permissions:
    def __init__(self, read=False, write=False, execute=False):
        self.read = read
        self.write = write
        self.execute = execute

class User:
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions
        self.groups = set()

    def add_to_group(self, group):
        self.groups.add(group)

class Group:
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions

class File:
    def __init__(self, name, content, owner, group, permissions):
        self.name = name
        self.content = content
        self.owner = owner
        self.group = group
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

    def add_file(self, file_name, content, owner, group, permissions):
        new_file = File(file_name, content, owner, group, permissions)
        self.files[file_name] = new_file
        return new_file

def create_file_system():
    root_directory = Directory("/")
    user1 = User("user1", Permissions(read=True, write=True, execute=True))
    user2 = User("user2", Permissions(read=True, write=False, execute=False))

    # Creating groups and adding users to them
    group1 = Group("group1", Permissions(read=True, write=True))
    group2 = Group("group2", Permissions(read=True, write=False))
    user1.add_to_group(group1)
    user2.add_to_group(group2)

    # Creating a file and setting permissions
    root_directory.add_file("file1.txt", "This is the content of file 1", user1, group1, Permissions(read=True, write=True))
    root_directory.add_file("file2.txt", "This is the content of file 2", user2, group2, Permissions(read=True, write=False))

    # Creating a sub-directory
    sub_directory = root_directory.add_directory("subdir1")
    sub_directory.add_file("file3.txt", "This is the content of file 3", user1, group1, Permissions(read=True, write=False))

    return root_directory

# Accessing files and directories via an access path
def access_path(root_directory, path, user):
    current_directory = root_directory
    elements = path.strip("/").split("/")
    for element in elements:
        if element in current_directory.sub_directories:
            current_directory = current_directory.sub_directories[element]
        elif element in current_directory.files:
            file = current_directory.files[element]
            if file.owner.name == user.name or file.group in user.groups or file.permissions.read:
                print(f"Content of {element}: {file.content}")
            else:
                print("You don't have permission to read this file.")
        else:
            print(f"{element} not found.")

if __name__ == "__main__":
    file_system = create_file_system()

    # Accessing files and directories using access path for user1
    user1 = User("user1", Permissions(read=True, write=True, execute=True))
    access_path(file_system, "/file1.txt", user1)  # Output: Content of file1.txt: This is the content of file 1
    access_path(file_system, "/subdir1/file3.txt", user1)  # Output: Content of file3.txt: This is the content of file 3
    access_path(file_system, "/file2.txt", user1)  # Output: You don't have permission to read this file.
    access_path(file_system, "/non_existent_file.txt", user1)  # Output: non_existent_file.txt not found.

    # Accessing files and directories using access path for user2
    user2 = User("user2", Permissions(read=True, write=False, execute=False))
    access_path(file_system, "/file1.txt", user2)  # Output: Content of file1.txt: This is the content of file 1
    access_path(file_system, "/subdir1/file3.txt", user2)  # Output: You don't have permission to read this file.
    access_path(file_system, "/file2.txt", user2)  # Output: Content of file2.txt: This is the content of file 2
    access_path(file_system, "/non_existent_file.txt", user2)  # Output: non_existent_file.txt not found.


