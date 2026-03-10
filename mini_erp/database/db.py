import sqlite3

def conectar():

    conn = sqlite3.connect("erp.db")
    return conn


def criar_tabelas():

    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute("""
INSERT INTO usuarios (username,password)
VALUES ('admin','1234')
""")
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    telefone TEXT,
    email TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    preco REAL,
    estoque INTEGER
    )
    """)

    conn.commit()
    conn.close()