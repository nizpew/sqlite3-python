import sqlite3

try:
    with sqlite3.connect("meu_banco.db") as conn:
        print(f"Banco de dados criado/aberto com sucesso, versão SQLite: {sqlite3.sqlite_version}")
except sqlite3.OperationalError as e:
    print("Erro ao abrir/criar banco de dados:", e)


with sqlite3.connect("meu_banco.db") as conn:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            idade INTEGER
        );
    """)
    conn.commit()
    print("Tabela criada com sucesso.")


with sqlite3.connect("meu_banco.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    for linha in cursor.fetchall():
        print(linha)


import sqlite3

def criar_banco():
    with sqlite3.connect("meu_banco.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                idade INTEGER
            );
        """)
        conn.commit()

def inserir_cliente(nome, email, idade):
    with sqlite3.connect("meu_banco.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clientes (nome, email, idade) VALUES (?, ?, ?)",
                       (nome, email, idade))
        conn.commit()

def listar_clientes():
    with sqlite3.connect("meu_banco.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes")
        for cliente in cursor.fetchall():
            print(cliente)

if __name__ == "__main__":
    criar_banco()
    inserir_cliente("Maria Oliveira", "maria@email.com", 25)
    inserir_cliente("Carlos Pereira", "carlos@email.com", 40)
    print("Clientes cadastrados:")
    listar_clientes()
