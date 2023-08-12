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

import sqlite3
import os


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

def initialize_database():
        conn = sqlite3.connect("filesystem.db")
        c = conn.cursor()

        c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        ''')

        c.execute('''
            CREATE TABLE IF NOT EXISTS groups (
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        ''')

        c.execute('''
            CREATE TABLE IF NOT EXISTS directories (
                id INTEGER PRIMARY KEY,
                name TEXT,
                parent_id INTEGER,
                FOREIGN KEY (parent_id) REFERENCES directories (id)
            )
        ''')

        c.execute('''
            CREATE TABLE IF NOT EXISTS files (
                id INTEGER PRIMARY KEY,
                name TEXT,
                content TEXT,
                directory_id INTEGER,
                owner_id INTEGER,
                group_id INTEGER,
                FOREIGN KEY (directory_id) REFERENCES directories (id),
                FOREIGN KEY (owner_id) REFERENCES users (id),
                FOREIGN KEY (group_id) REFERENCES groups (id)
            )
        ''')

        conn.commit()
        conn.close()

def add_user_to_database(username):
    conn = sqlite3.connect("filesystem.db")
    c = conn.cursor()

    # Insert the new username into the 'users' table
    c.execute("INSERT INTO users (name) VALUES (?)", (username,))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    file_system = FileSystem()
    initialize_database()
    
    # Create new groups and users
    group1 = Group("group1")
    group2 = Group("group2")
    user1 = User("user1")
    user2 = User("user2")

    new_username = input("Enter the new username or press enter: ")
    add_user_to_database(new_username)

    conn = sqlite3.connect("filesystem.db")
    c = conn.cursor()

    c.execute("INSERT INTO groups (name) VALUES (?)", (group1.name,))
    c.execute("INSERT INTO groups (name) VALUES (?)", (group2.name,))
    c.execute("INSERT INTO users (name) VALUES (?)", (user1.name,))
    c.execute("INSERT INTO users (name) VALUES (?)", (user2.name,))

    conn.commit()
    conn.close()

    user1.add_to_group(group1)
    user2.add_to_group(group2)

    logged_in_user = None

    # Interactive CLI Menu
    while True:
        print("Menu:")
        print("1. Login")
        print("2. Create Directory")
        print("3. Create File")
        print("4. Update Permissions")
        print("5. Delete File or Directory")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter your username: ")
            print(f"DEBUG - Username entered: {username}")

            # Logic to login the user using the file_system instance
            logged_in_user = file_system.login_user(username)
            print(f"DEBUG - Logged in user: {logged_in_user}")

            if logged_in_user:
                print(f"Logged in as {username}.")
            else:
                print(f"User {username} not found.")

        elif choice == "2":
            if logged_in_user is None:
                print("Please login before creating a directory.")
                continue

            parent_path = input("Enter parent path (e.g., '/dir1'): ")
            dir_name = input("Enter directory name: ")

            # Create a new directory using file_system instance
            file_system.create_directory(parent_path, dir_name)
            print(f"Directory '{dir_name}' created at '{parent_path}'.")

        elif choice == "3":
            if logged_in_user is None:
                print("Please login before creating a file.")
                continue

            dir_path = input("Enter directory path (e.g., '/dir1'): ")
            file_name = input("Enter file name: ")
            content = input("Enter file content: ")

            # Create a new file using file_system instance
            file_system.create_file(dir_path, file_name, content)
            print(f"File '{file_name}' created at '{dir_path}'.")

        elif choice == "4":
            if logged_in_user is None:
                print("Please login before updating permissions.")
                continue

            element_path = input("Enter element path (e.g., '/dir1'): ")
            read_perm = input("Set read permission (y/n): ").lower() == "y"
            write_perm = input("Set write permission (y/n): ").lower() == "y"

            # Set permissions using file_system instance
            file_system.set_permissions(element_path, read=read_perm, write=write_perm)
            print(f"Permissions updated for '{element_path}'.")

        elif choice == "5":
            if logged_in_user is None:
                print("Please login before deleting files or directories.")
                continue

            element_path = input("Enter element path to delete (e.g., '/dir1/file1.txt'): ")

            # Implement logic to delete file or directory using file_system instance
            # ... (delete logic)

        elif choice == "6":
            break
        else:
            print("Invalid choice. Please choose again.")

    # Updating permissions for groups
    group1.permissions.update_permissions(read=True, write=True)
    group2.permissions.update_permissions(read=True, write=False)

    # Login users to the file system
    file_system.login_user("user1")

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


