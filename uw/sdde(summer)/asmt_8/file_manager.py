import os
from models import Session, File

class FileManager:
    def create_file(self, directory, file_name):
        session = Session()
        
        new_file = File(name=file_name, directory=directory)
        session.add(new_file)
        session.commit()
        session.close()

        # Create the file in the root directory of the project
        root_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(root_directory, directory.name, file_name)
        with open(file_path, "w") as file:
            file.write("This is the content of the file.")

        print(f"File '{file_name}' created successfully in '{directory.name}'.")
        

    def delete_file(self, file):
        session = Session()
        
        session.delete(file)
        session.commit()
        print(f"File '{file.name}' deleted successfully.")
        session.close()
    
    def list_files(self, directory):
        session = Session()
        
        directory_files = session.query(File).filter_by(directory=directory).all()
        
        if directory_files:
            print(f"Files in '{directory.name}':")
            for index, file in enumerate(directory_files, start=1):
                print(f"{index}. {file.name}")
        else:
            print(f"No files found in '{directory.name}'.")
        
        session.close()

