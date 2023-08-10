from flask import render_template, request, redirect, url_for
from app import app
from .file_system import FileSystem, User, Group, access_path

# Create a file system instance
file_system = FileSystem()

# Sample data to simulate user and group setup
group1 = Group("group1")
group2 = Group("group2")
user1 = User("user1")
user2 = User("user2")
user1.add_to_group(group1)
user2.add_to_group(group2)
group1.permissions.update_permissions(read=True, write=True)
group2.permissions.update_permissions(read=True, write=False)
file_system.login_user(user1)

# Define routes and view functions

@app.route('/')
def index():
    return render_template('index.html', file_system=file_system)

@app.route('/create_directory', methods=['POST'])
def create_directory():
    path = request.form['path']
    directory_name = request.form['directory_name']
    file_system.create_directory(path, directory_name)
    return redirect(url_for('index'))

@app.route('/create_file', methods=['POST'])
def create_file():
    path = request.form['path']
    file_name = request.form['file_name']
    content = request.form['content']
    file_system.create_file(path, file_name, content)
    return redirect(url_for('index'))

@app.route('/set_permissions', methods=['POST'])
def set_permissions():
    path = request.form['path']
    read = 'read' in request.form
    write = 'write' in request.form
    execute = 'execute' in request.form
    file_system.set_permissions(path, read=read, write=write, execute=execute)
    return redirect(url_for('index'))

@app.route('/access_file', methods=['POST'])
def access_file():
    path = request.form['path']
    access_path(file_system.root_directory, path, file_system.logged_in_user)
    return redirect(url_for('index'))

@app.route('/update_file', methods=['POST'])
def update_file():
    path = request.form['path']
    content = request.form['content']
    file = file_system._get_element(path)
    if isinstance(file, File):
        file.content = content
    return redirect(url_for('index'))

@app.route('/rename_element', methods=['POST'])
def rename_element():
    path = request.form['path']
    new_name = request.form['new_name']
    element = file_system._get_element(path)
    if element:
        parent_directory = element.parent
        if isinstance(element, File):
            parent_directory.files[new_name] = parent_directory.files.pop(element.name)
        elif isinstance(element, Directory):
            parent_directory.sub_directories[new_name] = parent_directory.sub_directories.pop(element.name)
        element.name = new_name
    return redirect(url_for('index'))

@app.route('/delete_element', methods=['POST'])
def delete_element():
    path = request.form['path']
    element = file_system._get_element(path)
    if element:
        parent_directory = element.parent
        if isinstance(element, File):
            parent_directory.files.pop(element.name, None)
        elif isinstance(element, Directory):
            parent_directory.sub_directories.pop(element.name, None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)