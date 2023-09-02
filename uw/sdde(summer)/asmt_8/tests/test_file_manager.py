import pytest
from unittest.mock import patch, Mock
from file_manager import FileManager

# Define a test directory and files
test_directory = Mock(name="Test Directory")
test_files = [Mock(name=f"File {i}") for i in range(1, 4)]  # Replace with your actual file objects

def test_list_files():
    # Create an instance of the FileManager
    file_manager = FileManager()

    # Mock the database query to return the test_directory and test_files
    with patch('file_manager.Session') as mock_session:
        mock_session.query().filter_by().all.return_value = test_files

        # Call the list_files method
        with patch('builtins.print') as mock_print:
            file_manager.list_files(test_directory)

    # Assert that the method printed the correct messages
    expected_output = [
        f"Files in '{test_directory.name}':",
        "1. File 1",
        "2. File 2",
        "3. File 3"
    ]

    mock_print.assert_called_with(*expected_output)

# Run the tests
if __name__ == '__main__':
    pytest.main()
