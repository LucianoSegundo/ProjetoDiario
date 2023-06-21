import streamlit as st
import sqlite3
from datetime import datetime
from tela_registro import criptografar, descriptografar

# Função para verificar se o usuário está registrado no banco de dados
def verificar_usuario(nome_usuario, senha):
    conexao = sqlite3.connect("Projetodiario/banco/bandados.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT nome, senha FROM usuario WHERE nome=?", (criptografar(nome_usuario),))
    resultado = cursor.fetchone()

    conexao.close()

    if resultado is None:
        return False
    
    nome_registrado, senha_registrada = resultado
    if nome_registrado == criptografar(nome_usuario) and senha_registrada == criptografar(senha):
        return True
    
    return False

# Função para validar a data no formato dd/mm/yyyy
def validar_data(data_texto):
    try:
        datetime.strptime(data_texto, "%d/%m/%Y")
        return True
    except ValueError:
        return False

# Função para realizar o registro do relato
def registrar_relato(nome_usuario, titulo, data, relato):
    conexao = sqlite3.connect("Projetodiario/banco/bandados.db")
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO relatos (nome_usuario, data_relato, texto, titulo) VALUES (?, ?, ?, ?)",
                   (criptografar(nome_usuario), data, criptografar(relato), criptografar(titulo)))
    conexao.commit()

    conexao.close()

    return "Relato registrado com sucesso!"

# Interface da página de escrita de relatos
def tela_escrita():
    st.title("Escrita de Relatos")
    st.write("Preencha os campos abaixo para escrever um relato:")

    nome_usuario = st.text_input("Nome de Usuário", max_chars=20)
    senha = st.text_input("Senha", type="password", max_chars=10)

    titulo = st.text_input("Título")
    data = st.text_input("Data (dd/mm/yyyy)")

    relato = st.text_area("Relato", height=600, max_chars=3000)

    if st.button("Enviar"):
        if nome_usuario == "" or senha == "" or titulo == "" or data == "" or relato == "":
            st.error("Todos os campos devem ser preenchidos.")
        elif not verificar_usuario(nome_usuario, senha):
            st.error("Usuário não registrado ou senha incorreta.")
        elif not validar_data(data):
            st.error("Data inválida. O formato deve ser dd/mm/yyyy.")
        else:
            resultado = registrar_relato(nome_usuario, titulo, data, relato)
            st.success(resultado)
    
# Execução da interface do Streamlit
if __name__ == "__main__":
    tela_escrita()
