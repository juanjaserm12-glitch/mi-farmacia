import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def conectar_db():
    # Esto crea un archivo llamado 'farmacia.db' en tu carpeta
    conn = sqlite3.connect('farmacia.db')
    conn.row_factory = sqlite3.Row # Para que funcione como un diccionario
    return conn

# Crear la tabla automáticamente si no existe
def inicializar_db():
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS medicamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            compuesto TEXT,
            lote TEXT,
            material TEXT,
            precio REAL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM medicamentos ORDER BY id DESC')
    medicamentos = cur.fetchall()
    conn.close()
    return render_template('index.html', medicamentos=medicamentos)

if __name__ == '__main__':
    inicializar_db() # Crea la base de datos al iniciar
    app.run(debug=True, port=5000)