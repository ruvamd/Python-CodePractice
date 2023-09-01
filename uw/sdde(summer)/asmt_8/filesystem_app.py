from user_manager import UserManager
from directory_manager import DirectoryManager
from file_manager import FileManager
from models import Session,User, Directory, File


def main_menu():
    print("1. Create User")
    print("2. Login")
    print("3. Create Directory")
    print("4. Delete Directory")
    print("5. Update Directory")
    print("6. List Directories")
    print("7. Create File")
    print("8. Delete File")
    print("9. List Files")
    print("10. Exit")

def main():
    print("Welcome to the File System App!")

    user_manager = UserManager()
    directory_manager = DirectoryManager()
    file_manager = FileManager()

    user = None  # User object to track the logged-in user

    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            user_manager.create_user(username, password)
        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            user = user_manager.login(username, password)
        elif user:
            if choice == '3':
                directory_name = input("Enter directory name: ")
                user_id = user  # Store user ID
                directory_manager.create_directory(user.id, directory_name)  # Pass user ID

            elif choice == '4':
                user_directories = directory_manager.list_directories(user)
                if user_directories:
                    dir_index = int(input("Enter the index of the directory to delete: "))
                    if 1 <= dir_index <= len(user_directories):
                        directory_manager.delete_directory(user_directories[dir_index - 1])
                    else:
                        print("Invalid index.")

            elif choice == '5':
                user_directories = directory_manager.list_directories(user)
                if user_directories:
                    dir_index = int(input("Enter the index of the directory to update: "))
                    if 1 <= dir_index <= len(user_directories):
                        new_name = input("Enter the new name for the directory: ")
                        directory_manager.update_directory(user_directories[dir_index - 1], new_name)
                    else:
                        print("Invalid index.")

            elif choice == '6':
                user_directories = directory_manager.list_directories(user)
                if user_directories:
                    print("User Directories:")
                    for index, directory in enumerate(user_directories, start=1):
                        print(f"{index}. {directory.name}")
                        print()
                else:
                    print("No directories found for this user.")

            elif choice == '7':
                if user:
                    user_directories = directory_manager.list_directories(user)
                    if user_directories:
                        dir_index = int(input("Enter the index of the directory to add a file to: "))
                        if 1 <= dir_index <= len(user_directories):
                            directory = user_directories[dir_index - 1]
                            session = Session()  # Create a new session
                            directory_from_db = session.query(Directory).get(directory.id)  # Retrieve directory from the session
                            session.close()  # Close the session
                            file_name = input("Enter the name of the file: ")
                            file_manager.create_file(directory_from_db, file_name)
                        else:
                            print("Invalid index.")
                    else:
                        print("No directories found for this user.")
                else:
                    print("Please log in first.")

            elif choice == '8':
                user_directories = directory_manager.list_directories(user)
                if user_directories:
                    dir_index = int(input("Enter the index of the directory to delete a file from: "))
                    if 1 <= dir_index <= len(user_directories):
                        directory = user_directories[dir_index - 1]
                        directory_files = file_manager.list_files(directory)
                        if directory_files:
                            file_index = int(input("Enter the index of the file to delete: "))
                            if 1 <= file_index <= len(directory_files):
                                file_manager.delete_file(directory_files[file_index - 1])
                            else:
                                print("Invalid file index.")
                        else:
                            print("No files to delete in this directory.")
                    else:
                        print("Invalid directory index.")

            elif choice == '9':
                    user_directories = directory_manager.list_directories(user)
                    if user_directories:
                        dir_index = int(input("Enter the index of the directory to list files from: "))
                        if 1 <= dir_index <= len(user_directories):
                            directory = user_directories[dir_index - 1]
                            file_manager.list_files(directory)
                        else:
                            print("Invalid directory index.")

            elif choice == '10':
                    print("Exiting the app. Goodbye!")
                    break
            else:
                print("Invalid choice. Please select a valid option.")        
        else:
            print("Please log in first.")

if __name__ == "__main__":
    main()

