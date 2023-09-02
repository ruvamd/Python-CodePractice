import os
from models import Session, File, Directory

class FileManager:
    def create_file(self, user, directory_name, file_name):
        session = Session()
        
        # Check if the user has a directory with the specified name
        directory = session.query(Directory).filter_by(owner=user, name=directory_name).first()
        if not directory:
            print(f"Directory '{directory_name}' not found for this user.")
            session.close()
            return
        
        # Get the user's home directory
        user_home_directory = os.path.expanduser("~")
        
        # Create the directory on the user's machine if it doesn't exist
        directory_path = os.path.join(user_home_directory, directory_name)
        os.makedirs(directory_path, exist_ok=True)
        
        # Create the file within the directory
        file_path = os.path.join(directory_path, file_name)
        
        try:
            with open(file_path, 'w') as file:
                file.write("This is the content of the file.")
        except Exception as e:
            print(f"Error creating file '{file_name}': {str(e)}")
            session.close()
            return

        # Create a file record in the database
        new_file = File(name=file_name, directory=directory)
        session.add(new_file)
        
        session.commit()
        print(f"File '{file_name}' created successfully in '{directory_name}'.")
        session.close()
        

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

