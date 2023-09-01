from models import Session,User, Directory  # Import User and Directory classes
import os

class DirectoryManager:
    def create_directory(self, user_id, directory_name):
        session = Session()

        user = session.query(User).get(user_id)  # Retrieve user object using user ID
        new_directory = Directory(name=directory_name, owner=user)
        session.add(new_directory)
        session.commit()
        session.close()

        # Create the directory in the root directory of the project
        root_directory = os.path.dirname(os.path.abspath(__file__))
        directory_path = os.path.join(root_directory, directory_name)
        os.makedirs(directory_path)
        print(f"Directory '{directory_name}' created successfully.")
        

    def delete_directory(self, directory):
        session = Session()
        
        # Delete the directory from the database
        session.delete(directory)
        session.commit()
        print(f"Directory '{directory.name}' deleted successfully from the database..")
        session.close()

        # Delete the directory from the root directory
        root_directory = os.path.join(os.getcwd(), directory.name)
        try:
            os.rmdir(root_directory)
            print(f"Directory '{directory.name}' deleted successfully from the root directory.")
        except OSError:
            print(f"Error deleting directory '{directory.name}' from the root directory.")

    def update_directory(self, directory, new_name):
        session = Session()
        
        directory.name = new_name
        session.commit()
        print(f"Directory name updated to '{new_name}'.")
        session.close()
    
    def list_directories(self, user):
        session = Session()

        user_directories = session.query(Directory).filter(Directory.owner_id == user.id).all()

        session.close()

        return user_directories


        

