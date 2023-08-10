class FileSystem:
    def __init__(self):
        self.root_directory = Directory("/")
        self.logged_in_user = None

    def login_user(self, user):
        self.logged_in_user = user

    @app.route("/create_directory", methods=["POST"])
    def create_directory():
        if file_system.logged_in_user:
            path = request.form["path"]
            directory_name = request.form["directory_name"]
            file_system.create_directory(path, directory_name)
            return redirect(url_for("home"))
        else:
            return "Please login to create a directory."

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
            if not element:
                continue  # Skip empty elements
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

# Before attempting to access a directory or file, print the constructed path
def access_path(root_directory, path, user):
    current_element = root_directory
    elements = path.strip("/").split("/")
    print(f"Accessing path: {path}")  # Add this line
    for element in elements:
        if element in current_element.sub_directories:
            current_element = current_element.sub_directories[element]
        elif element in current_element.files:
            file = current_element.files[element]
            file.access(user)
        else:
            print(f"{element} not found.")
