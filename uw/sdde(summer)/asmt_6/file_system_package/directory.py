from .file_system_element import FileSystemElement
from .file import File
from .models import Directory, Group, Permissions  # Import other necessary models

class Directory(FileSystemElement):
    def __init__(self, name):
        super().__init__(name)
        self.sub_directories = {}
        self.files = {}
        self.group = Group(name)  # Each directory has its own group
        self.permissions = Permissions(owner=self.group, group=self.group)
        self.type = "directory"

    def add_directory(self, directory_name):
        new_directory = Directory(directory_name, self)
        self.sub_directories[directory_name] = new_directory
        return new_directory

    def add_file(self, file_name, content, owner, group):
        new_file = File(file_name, content, owner, group)
        self.files[file_name] = new_file
        return new_file

    def _add_to_path(self, path, directory, session):
        current_element = self.root_directory
        elements = path.strip("/").split("/")
        parent_id = None  # This will store the parent directory's ID

        conn = session.connection()
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

    def access(self, user):
        print(f"Accessing directory: {self.name}")