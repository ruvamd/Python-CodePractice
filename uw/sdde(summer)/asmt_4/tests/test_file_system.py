import pytest
from file_system_package.file_system import FileSystem,Directory,User,Group

@pytest.fixture
def empty_file_system():
    return FileSystem()

@pytest.fixture
def populated_file_system():
    file_system = FileSystem()
    
@pytest.fixture
def populated_file_system():
    file_system = FileSystem()

    # Create users
    user1 = User("user1")
    user2 = User("user2")

    # Create groups
    group1 = Group("group1")
    group2 = Group("group2")

    # Add users to groups
    user1.add_to_group(group1)
    user2.add_to_group(group2)

    # Log in a user
    file_system.login_user("user1")

    # Create directories
    file_system.create_directory("/", "dir1")
    file_system.create_directory("/dir1", "dir2")
    file_system.create_directory("/dir1/dir2", "dir3")

    # Create files
    file_system.create_file("/dir1", "file1.txt", "Content of file 1")
    file_system.create_file("/dir1/dir2", "file2.txt", "Content of file 2")

    # Set permissions for directories and files
    file_system.set_permissions("/", read=True)
    file_system.set_permissions("/dir1", read=True, write=True)
    file_system.set_permissions("/dir1/dir2", write=True)

    return file_system

def test_login_user():
    file_system = FileSystem()

    # Test login with an existing user
    user = file_system.login_user("user1")
    assert user is not None

    # Test login with a non-existing user
    non_existing_user = file_system.login_user("non_existing_user")
    assert non_existing_user is None

def test_create_directory():
    file_system = FileSystem()

    # Test creating a directory with a logged-in user
    file_system.login_user("user1")
    file_system.create_directory("/", "test_dir")
    assert file_system.directory_exists("/test_dir")

    # Test creating a directory without logging in
    file_system.logged_in_user = None
    file_system.create_directory("/", "test_dir_2")
    assert not file_system.directory_exists("/test_dir_2")

def test_create_file(populated_file_system):
    file_system = populated_file_system
    file_system.login_user("user1")
    file_system.create_file("/dir1", "new_file.txt", "New file content")
    directory = file_system._get_directory("/dir1")
    assert "new_file.txt" in directory.files

def test_create_file_no_login(populated_file_system, capsys):
    file_system = populated_file_system
    file_system.create_file("/dir1", "new_file.txt", "New file content")
    captured = capsys.readouterr()
    assert "Please login before creating a file." in captured.out

def test_list_files(populated_file_system, capsys):
    file_system = populated_file_system
    file_system.login_user("user1")
    file_system.list_files("/dir1")
    captured = capsys.readouterr()
    assert "File: file1.txt" in captured.out

def test_list_files_no_login(populated_file_system, capsys):
    file_system = populated_file_system
    file_system.list_files("/dir1")
    captured = capsys.readouterr()
    assert "Please login to the file system before listing files." in captured.out

def test_set_permissions(populated_file_system):
    file_system = populated_file_system
    file_system.login_user("user1")
    file_system.set_permissions("/dir1", read=True, write=True)
    directory = file_system._get_directory("/dir1")
    file = directory.files["file1.txt"]
    assert file.group.permissions.read
    assert file.group.permissions.write

def test_delete_file(populated_file_system):
    file_system = populated_file_system
    file_system.login_user("user1")
    file_system.delete_element("/dir1/file1.txt")
    directory = file_system._get_directory("/dir1")
    assert "file1.txt" not in directory.files

def test_delete_directory(populated_file_system):
    file_system = populated_file_system
    file_system.login_user("user1")
    file_system.delete_element("/dir1/dir2")
    directory = file_system._get_directory("/dir1")
    assert "dir2" not in directory.sub_directories

def test_delete_no_login(populated_file_system, capsys):
    file_system = populated_file_system
    file_system.delete_element("/dir1/file1.txt")
    captured = capsys.readouterr()
    assert "Please login before deleting files or directories." in captured.out

def test_access_file(populated_file_system, capsys):
    file_system = populated_file_system
    file_system.login_user("user1")
    file_system.access_element("/dir1/file1.txt")
    captured = capsys.readouterr()
    assert "Content of file1.txt" in captured.out

def test_access_file_no_permission(populated_file_system, capsys):
    file_system = populated_file_system
    file_system.login_user("user2")
    file_system.access_element("/dir1/file1.txt")
    captured = capsys.readouterr()
    assert "You don't have permission to read this file." in captured.out

def test_check_directory_existence(populated_file_system):
    file_system = populated_file_system
    assert file_system.directory_exists("/dir1")

def test_check_directory_not_existence(populated_file_system):
    file_system = populated_file_system
    assert not file_system.directory_exists("/nonexistent")
