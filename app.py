from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for flash messages

# ========== CONFIGURATION ==========
BASE_DIR = os.getcwd()
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
TASKS_FILE = os.path.join(BASE_DIR, 'data', 'tasks.txt')
SUBJECTS_FILE = os.path.join(BASE_DIR, 'data', 'subjects.txt')

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(os.path.dirname(TASKS_FILE), exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ========== ROUTES ==========

@app.route('/')
def splash():
    return render_template('splash.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/notes', methods=['GET', 'POST'])
def notes():
    if request.method == 'POST':
        uploaded_file = request.files.get('note')
        if uploaded_file and uploaded_file.filename:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
            uploaded_file.save(file_path)
            flash(f"✅ '{uploaded_file.filename}' uploaded successfully.")
            return redirect(url_for('notes'))
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('notes.html', files=files)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/delete/<filename>')
def delete_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        flash(f"🗑️ '{filename}' deleted successfully.")
    else:
        flash(f"⚠️ File '{filename}' not found.")
    return redirect(url_for('notes'))

@app.route('/subjects', methods=['GET', 'POST'])
def subjects():
    if request.method == 'POST':
        new_subject = request.form.get('subject')
        if new_subject:
            with open(SUBJECTS_FILE, 'a') as f:
                f.write(new_subject + '\n')
            flash(f"📘 Subject '{new_subject}' added.")
            return redirect(url_for('subjects'))
    subjects = []
    if os.path.exists(SUBJECTS_FILE):
        with open(SUBJECTS_FILE, 'r') as f:
            subjects = [line.strip() for line in f.readlines() if line.strip()]
    return render_template('subjects.html', subjects=subjects)

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            with open(TASKS_FILE, 'a') as f:
                f.write(task + '\n')
            flash(f"✅ Task added: '{task}'")
            return redirect(url_for('tasks'))
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            tasks = [line.strip() for line in f.readlines() if line.strip()]
    return render_template('tasks.html', tasks=tasks)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# ========== RUN APP ==========
if __name__ == '__main__':
    app.run(debug=True)
