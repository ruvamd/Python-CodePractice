from unittest.mock import patch
import pytest
from file_manager import FileManager
from models import Session, File, Directory, User



# Mock the Session class and its methods
class MockSession:
    def add(self, obj):
        pass

    def commit(self):
        pass

    def close(self):
        pass

# Mock the FileManager class to use the mock session
class MockFileManager(FileManager):
    def __init__(self):
        self.session = MockSession()

@pytest.fixture
def mock_file_manager():
    return MockFileManager()

@patch('file_manager.Session', new_callable=MockSession)
def test_create_file(mock_session, mock_file_manager):
    # Create a mock user and directory
    user = User(id=1, username='testuser', password='testpassword')
    directory = Directory(id=1, name='testdir', owner=user)
    
    # Call the create_file method
    mock_file_manager.create_file(directory, 'testfile.txt')
    
    # Check if the session's add and commit methods were called
    assert mock_session.add.called
    assert mock_session.commit.called
