'''
prerequisite:
Design *nix File System. Class Structure
Explain the data structures and algorithms that you would use to design an
in-memory file system (Similar to *nix systems). Illustrate with an
example in code where possible. Your design must include the following
concepts Directory, File, User and Permissions. Please note there can be
other concepts in your design but these ones are required.
Use cases that must be supported by your design:
Machine Startup & File System instantiation
Access to all the files and directories via an access path
Setting permissions and reading permissions
Creating/Reading/Updating/Deleting a Directory or a File
Rubric:
Complete class structure (1 point)
Relationships between classes (1 point)
Appropriate class variables to store the file system details (1 point)
Appropriate methods signatures in the classes that support the following
use cases (2 points)
Feedback - >
Requirements
1. Groups
2. Instantitaion
3. User Permissions
Clarifying Questions
1. Can we have two files with the same name/type?
A. Yes.
2. Can a user create other users?
A. User with an Admin role can create other users?
3. What permissions can be specified?
A. Admin user can set the permissions for a user.
--------------------------------------------------------------------------
------------------
Files
- Extension/Types
- Content/Data
- Size #
- Name #
- Unique_Id
- Create_Date #
- Modified_Date #
- Permissions #
- Physical_Address
Directories
- Root
- Parents
- Children
- Directories : Lists
- Files : Lists
- Name #
- Create_Date #
- Modified_Date #
-*Permissions #
- Size #
Permissions
- Read
- Write
- Execute
- Delete
- Create
User
- Name
- Groups
- Role
~ Permissions
- Admin
- Regular
Group
- Users : List
- Id
FileSystem
- Directory -> Root
User Session
- User
CRUD on Files
Execute on Files
CRUD on Directories
CRUD Permissions
CRUD on Users
CRUD on Groups
File system could be extended to use Links
'''

'''
"createDirectory" method actually does make sense in the "Directory" class
instead of the "FileSystem" class. The "FileSystem" class could just instantiate
a specific Directory as "root" directory but we don't need the method there. 
So change this code reflected in the code that uploaded.

rewrite following code in python.
'''

'''
class FileSystem {
FileSystem () {
Root = new Directory (/* values */ )
/* Values
In case of 'root'
name = '/'
id = 0
user = system
parent = null
permissions = Read
*/
}
Directory Root;
}
interface FileSystemEntry {
int id;
String name;
Long Size;
Date create_date;
Date modified_date;
Permissions permission;
FileSystemEntry parent;
}
class Directoy implements FileSystemEntry {
FileSystemEntry [] children;
public Directory createDirectory(String name, int id, User user,
FileSystemEntry parent, Permissions permissions) {
Directory direcotry = new Directory
}
}
class File implements FileSystemEntry {
String type;
String physical_address;
}
'''
from enum import Enum
from datetime import datetime

class Permissions(Enum):
    READ = 1
    WRITE = 2
    EXECUTE = 4
    DELETE = 8
    CREATE = 16

class FileSystemEntry:
    def __init__(self, name, size, parent, permissions):
        self.name = name
        self.size = size
        self.create_date = datetime.now()
        self.modified_date = datetime.now()
        self.permissions = permissions
        self.parent = parent

class Directory(FileSystemEntry):
    def __init__(self, name, size, parent, permissions):
        super().__init__(name, size, parent, permissions)
        self.children = []

    def create_directory(self, name, size, permissions):
        directory = Directory(name, size, self, permissions)
        self.children.append(directory)
        return directory

class File(FileSystemEntry):
    def __init__(self, name, size, parent, permissions, file_type, physical_address):
        super().__init__(name, size, parent, permissions)
        self.type = file_type
        self.physical_address = physical_address

class User:
    def __init__(self, name, groups, role):
        self.name = name
        self.groups = groups
        self.role = role

class Group:
    def __init__(self, group_id):
        self.group_id = group_id
        self.users = []

class FileSystem:
    def __init__(self):
        self.root = Directory('/', 0, None, Permissions.READ.value)

    def create_user(self, name, groups, role):
        return User(name, groups, role)

    def create_group(self, group_id):
        return Group(group_id)

    def find_entry_by_path(self, path):
        current_entry = self.root
        if path == '/':
            return current_entry

        path_parts = path.strip('/').split('/')
        for part in path_parts:
            found_entry = None
            for child in current_entry.children:
                if child.name == part:
                    found_entry = child
                    break
            if found_entry is None or not isinstance(found_entry, Directory):
                return None
            current_entry = found_entry
        return current_entry

# Example usage:
fs = FileSystem()

# Creating users and groups
admin_group = fs.create_group('admin_group')
regular_group = fs.create_group('regular_group')

admin_user = fs.create_user('admin', [admin_group, regular_group], 'Admin')
regular_user = fs.create_user('user1', [regular_group], 'Regular')

# Creating directories and files
root_directory = fs.root
documents_directory = root_directory.create_directory('Documents', 0, Permissions.READ.value | Permissions.WRITE.value)
photos_directory = root_directory.create_directory('Photos', 0, Permissions.READ.value | Permissions.WRITE.value)
text_file = File('document.txt', 1024, documents_directory, Permissions.READ.value | Permissions.WRITE.value, 'txt', '/path/to/document.txt')

# Accessing files and directories via path
path = '/Documents/document.txt'
entry = fs.find_entry_by_path(path)
if entry:
    print(f"Accessing: {entry.name}, Permissions: {entry.permissions}")
else:
    print("Path not found.")

# Setting permissions
text_file.permissions = Permissions.READ.value

# Reading permissions
print(f"File Permissions: {text_file.permissions}")
