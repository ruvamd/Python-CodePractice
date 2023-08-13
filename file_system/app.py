import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Database initialization
db_connection = sqlite3.connect('filesystem.db')
db_cursor = db_connection.cursor()
db_cursor.execute('CREATE TABLE IF NOT EXISTS files (id INTEGER PRIMARY KEY, name TEXT, content TEXT)')
db_connection.commit()

# Routes
@app.route('/')
def index():
    db_cursor.execute('SELECT id, name FROM files')
    files = db_cursor.fetchall()
    return render_template('index.html', files=files)

@app.route('/create', methods=['POST'])
def create_file():
    name = request.form['filename']
    content = request.form['content']

    db_cursor.execute('INSERT INTO files (name, content) VALUES (?, ?)', (name, content))
    db_connection.commit()

    return redirect(url_for('index'))

@app.route('/file/<int:file_id>')
def view_file(file_id):
    db_cursor.execute('SELECT name, content FROM files WHERE id = ?', (file_id,))
    file_data = db_cursor.fetchone()
    return render_template('file.html', file_data=file_data)

if __name__ == '__main__':
    app.run(debug=True)
