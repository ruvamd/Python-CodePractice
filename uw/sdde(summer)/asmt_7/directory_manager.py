from models import Session,User, Directory  # Import User and Directory classes

class DirectoryManager:
    def create_directory(self, user_id, directory_name):
        session = Session()

        user = session.query(User).get(user_id)  # Retrieve user object using user ID
        new_directory = Directory(name=directory_name, owner=user)
        session.add(new_directory)

        session.commit()
        print(f"Directory '{directory_name}' created successfully.")
        session.close()

    def delete_directory(self, directory):
        session = Session()
        
        session.delete(directory)
        session.commit()
        print(f"Directory '{directory.name}' deleted successfully.")
        session.close()
    
    def update_directory(self, directory, new_name):
        session = Session()
        
        directory.name = new_name
        session.commit()
        print(f"Directory name updated to '{new_name}'.")
        session.close()
    
    def list_directories(self, user):
        session = Session()
        
        user_directories = session.query(Directory).filter_by(owner=user).all()
        
        if user_directories:
            print("User Directories:")
            for index, directory in enumerate(user_directories, start=1):
                print(f"{index}. {directory.name}")
        else:
            print("No directories found for this user.")
        
        session.close()
