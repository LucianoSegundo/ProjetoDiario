import streamlit as st
import sqlite3


def autenticar_usuario(nome, senha):
    conexao = sqlite3.connect("banco/bandados.db")
    cursor = conexao.cursor()

    # Verificar se o usuário e senha estão corretos
    cursor.execute(
        "SELECT nome FROM usuario WHERE nome = ? AND senha = ?", (nome, senha))
    resultado = cursor.fetchone()

    # Fechar a conexão com o banco de dados
    conexao.close()

    if resultado is not None:
        return True
    else:
        return False


def obter_relatos(nome_usuario, mes=None, letra=None):
    # Conexão com o banco de dados
    conexao = sqlite3.connect("banco/bandados.db")
    cursor = conexao.cursor()

    # Query para obter os relatos vinculados ao usuário
    query = "SELECT titulo, data_relato FROM relatos WHERE nome_usuario = ?"
    params = (nome_usuario,)

    # Filtrar pela primeira letra do título, se fornecida
    if letra:
        query += " AND titulo LIKE ?"
        params += (f"{letra}%",)

    # Ordenar por ordem alfabética do título
    query += " ORDER BY titulo"

    # Executar a query
    cursor.execute(query, params)
    relatos = cursor.fetchall()

    # Fechar a conexão com o banco de dados
    conexao.close()

    return relatos


def exibir_relato(nome_usuario, titulo):
    conexao = sqlite3.connect("banco/bandados.db")
    cursor = conexao.cursor()

    # Obter o relato completo com base no nome do usuário e título
    cursor.execute(
        "SELECT texto FROM relatos WHERE nome_usuario = ? AND titulo = ?", (nome_usuario, titulo))
    relato = cursor.fetchone()[0]

    # Fechar a conexão com o banco de dados
    conexao.close()

    # Exibir o relato
    st.subheader(titulo)
    st.write(relato)


def tela_leitura():
    # Interface de usuário
    st.title("Aplicação de Leitura de Relatos")
    nome = st.text_input("Nome de usuário:")
    senha = st.text_input("Senha:", type="password")
    validar = st.button("Validar")

    if validar:
        if autenticar_usuario(nome, senha):
            st.success("Credenciais válidas!")

        else:
            st.error("Credenciais inválidas!")
            st.stop()

    st.subheader("Lista de relatos")
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
              'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    letra_selecionada = st.selectbox(
        "Selecione uma letra para filtrar", ["Todos"] + letras)

    # Obter relatos filtrados pela primeira letra do título
    if letra_selecionada != "Todos":
        relatos = obter_relatos(nome, letra=letra_selecionada)
    else:
        relatos = obter_relatos(nome)
    # Exibir os relatos
    for relato in relatos:
        titulo = relato[0]
        data_relato = relato[1]
        if st.button(f"{titulo} - {data_relato}".title()):
            exibir_relato(nome, titulo)


# Executar a função tela_escrita
if __name__ == "__main__":
    tela_leitura()
