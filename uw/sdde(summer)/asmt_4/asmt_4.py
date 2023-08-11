'''
Using SQLite as the persistance for the directories/files,compile code into a functioning application. 
This application should be executable.The executable should be in web ui.

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
#from asmt_3 
'''
Refactor (add classess/method signatures) the code submitted in the previous 
assignment to include the following functionality.

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
'''

from file_system_package.file_system_element import FileSystemElement
from file_system_package.file import File
from file_system_package.directory import Directory
from file_system_package.user import User
from file_system_package.group import Group
from file_system_package.permissions import Permissions
from file_system_package.file_system import FileSystem

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


'''
specify what parts of code are using the objects that have already defined.

User Interface/API classes/methods:
Permissions: This class is used to manage the permissions of files and directories. 
It has methods to update permissions and follows the Singleton pattern to ensure only 
one instance of the class exists.

User: Represents a user and has a method to add the user to a group.

Group: Represents a group and has a Permissions object to manage group-level permissions.

FileSystemElement: The base class for both File and Directory, representing a generic 
file system element.

File: Represents a file and inherits from FileSystemElement. It has an access method 
to check if a user has permission to read the file and prints the content if allowed.

Directory: Represents a directory and inherits from FileSystemElement. It can contain 
sub-directories and files, and it also has an access method to print a message when accessing it.

Persistence classes/methods:
The code doesn't include any explicit persistence-related classes or methods, as the 
file system data is not stored persistently in files or databases. However, there is 
a FileSystem class that manages the file system and users' interactions with it, 
which can be considered as a high-level persistence class.

Judicious use of SOLID principles:
Single Responsibility Principle (SRP): Each class has a clear and single responsibility, 
such as managing permissions, representing users, files, directories, or the file system 
itself.

Open/Closed Principle (OCP): The classes are designed to be easily extensible without 
modifying existing code. For example, I can create new types of file system elements 
by subclassing FileSystemElement.

Liskov Substitution Principle (LSP): Subclasses like File and Directory can be used 
interchangeably with their base class FileSystemElement.

Interface Segregation Principle (ISP): The code doesn't explicitly define interfaces, 
but each class has a specific set of methods and attributes related to its purpose.

Dependency Inversion Principle (DIP): The code doesn't show explicit dependency injection, 
but it has well-defined relationships between classes, and the FileSystem class uses and 
depends on other classes like User, File, and Directory.

The code follows good principles of object-oriented design and keeps the responsibilities 
of each class well-defined, making it maintainable and extensible.
'''