from file_system_package.file import File
from file_system_package.directory import Directory
from user import User
from group import Group

from asmt_6.sql_alchemy import get_session
from file_system_package.models import User # Import other necessary models

class FileSystem:
    def __init__(self):
        self.root_directory = Directory("/")
        self.logged_in_user = None

    def login_user(self, username):
        with get_session() as session:
            user = session.query(User).filter_by(name=username).first()

            if user:
                self.logged_in_user = user
                return user
            else:
                return None

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

        # List the sub-directory names
        directory = self._get_directory(path)
        if directory:
            print(f"Listing sub-directories of directory: {path}")
            for name in directory.sub_directories:
                print(f"Directory: {name}")
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
            if element and element in current_element.sub_directories:
                current_element = current_element.sub_directories[element]
            elif element and element in current_element.files:
                current_element = current_element.files[element]
            else:
                return None
        return current_element

    def _add_to_path(self, path, directory):
        current_element = self.root_directory
        elements = path.strip("/").split("/")
        parent_id = None  # This will store the parent directory's ID

        conn = sqlite3.connect("filesystem.db")
        c = conn.cursor()

        for element in elements:
            if element in current_element.sub_directories:
                parent_id = current_element.sub_directories[element].id
                current_element = current_element.sub_directories[element]
            else:
                print(f"{element} not found.")
                conn.close()
                return

        # Insert the directory into the database
        c.execute("INSERT INTO directories (name, parent_id) VALUES (?, ?)", (directory.name, parent_id))
        conn.commit()
        conn.close()

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

    def directory_exists(self, path):
        conn = sqlite3.connect("filesystem.db")
        c = conn.cursor()

        # Query the directories table to check if the directory exists
        c.execute("SELECT id FROM directories WHERE name = ?", (path,))
        directory_id = c.fetchone()

        conn.close()

        return directory_id is not None
    
    