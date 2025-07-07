import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

# Create notes table
c.execute('''
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT,
        date TEXT
    )
''')

# Create tasks table
c.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT,
        done BOOLEAN
    )
''')

# Create subjects table
c.execute('''
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
''')

conn.commit()
conn.close()

print("✅ Database and tables created successfully!")
