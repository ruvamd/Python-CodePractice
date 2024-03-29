from models import Session, File

class FileManager:
    def create_file(self, directory, file_name):
        session = Session()
        
        new_file = File(name=file_name, directory=directory)
        session.add(new_file)
        
        session.commit()
        print(f"File '{file_name}' created successfully in '{directory.name}'.")
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

