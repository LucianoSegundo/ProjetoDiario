import sqlite3


try:
    # Conexão com o banco de dados
    conexao = sqlite3.connect("banco/bandados.db")
    cursor = conexao.cursor()

    # Criação da tabela "usuario"
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuario(
            nome TEXT(20) PRIMARY KEY NOT NULL,
            senha TEXT(10) NOT NULL
        )
    """)

    # Criação da tabela "relatos"
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS relatos(
            id_relato INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_usuario TEXT NOT NULL,
            data_relato DATE NOT NULL,
            texto TEXT(3000) NOT NULL,
            titulo TEXT(100) NOT NULL,
            FOREIGN KEY (nome_usuario) REFERENCES usuario (nome)
        )
    """)

    # Fechamento da conexão com o banco de dados
    conexao.close()

    print("Tabelas criadas com sucesso!")

except sqlite3.Error as e:
    print("Erro ao criar tabelas:", e)

