import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.mkdir('PythonPrograms')

  # Create the new file inside of the new directory
  os.chdir('PythonPrograms')
  with open('script.py','w') as file:
    pass
  os.chdir('..')

  # Return the list of files in the new directory
  return os.listdir('PythonPrograms')

print(new_directory("PythonPrograms", "script.py"))