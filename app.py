from flask import Flask, render_template, request, redirect, url_for
import os
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# --- Database Connection ---
def get_db_connection():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    return conn

# --- Splash Redirect ---
@app.route('/')
def index():
    return redirect(url_for('splash'))

@app.route('/splash')
def splash():
    return render_template('splash.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

# --- Notes Module ---
@app.route('/notes')
def notes():
    conn = get_db_connection()
    notes = conn.execute('SELECT * FROM notes').fetchall()
    conn.close()
    return render_template('notes.html', notes=notes)

@app.route('/add_note', methods=['POST'])
def add_note():
    title = request.form['title']
    content = request.form['content']
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = get_db_connection()
    conn.execute('INSERT INTO notes (title, content, date) VALUES (?, ?, ?)', (title, content, date))
    conn.commit()
    conn.close()
    return redirect(url_for('notes'))

# --- Tasks Module ---
@app.route('/tasks')
def tasks():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return render_template('tasks.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form['task']
    conn = get_db_connection()
    conn.execute('INSERT INTO tasks (task, done) VALUES (?, ?)', (task, False))
    conn.commit()
    conn.close()
    return redirect(url_for('tasks'))

@app.route('/update_task/<int:task_id>')
def update_task(task_id):
    conn = get_db_connection()
    conn.execute('UPDATE tasks SET done = NOT done WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('tasks'))

@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('tasks'))

# --- Subjects Module ---
@app.route('/subject', methods=['GET'])
def subject():
    conn = get_db_connection()
    subjects = conn.execute('SELECT * FROM subjects').fetchall()
    conn.close()
    return render_template('subject.html', subjects=subjects)

@app.route('/add_subject', methods=['POST'])
def add_subject():
    name = request.form['subject']
    conn = get_db_connection()
    conn.execute('INSERT INTO subjects (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()
    return redirect(url_for('subject'))

# --- Run App ---
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

