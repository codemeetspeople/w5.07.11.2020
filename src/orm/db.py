import sqlite3
import os

ORM_PATH = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(ORM_PATH, 'db.sqlite')

SELECT_QUERY = 'SELECT author, title FROM book WHERE id = ?'
INSERT_QUERY = 'INSERT INTO book (title, author) VALUES (?,?)'
UPDATE_QUERY = 'UPDATE book SET title = ?, author = ? WHERE id = ?'

connection = None


def get_connection():
    global connection

    if not connection:
        connection = sqlite3.connect(DATABASE_PATH, isolation_level=None)
    return connection


def create_db():
    conn = get_connection()
    cursor = conn.cursor()

    CREATE_TABLE = (
        'CREATE TABLE IF NOT EXISTS book ('
        '   id INTEGER PRIMARY KEY AUTOINCREMENT,'
        '   title VARCHAR(100) NOT NULL,'
        '   author VARCHAR(100) NOT NULL'
        ');'
    )

    cursor.execute(CREATE_TABLE)


create_db()
