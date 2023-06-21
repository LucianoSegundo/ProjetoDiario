import subprocess
import streamlit as st
import sqlite3

# Método para criptografar uma string
def criptografar(texto):
    # Implemente a lógica de criptografia aqui
    return texto

# Método para descriptografar uma string
def descriptografar(texto):
    # Implemente a lógica de descriptografia aqui
    return texto

# Função para verificar se a senha atende aos requisitos
def verificar_senha(senha):
    if len(senha) < 6 or len(senha) > 10:
        return False
    if not any(char.isupper() for char in senha):
        return False
    if not any(char.islower() for char in senha):
        return False
    if not any(char.isdigit() for char in senha):
        return False
    return True

# Função para verificar se o nome de usuário já está em uso

def verificar_nome_usuario(nome_usuario):
    
    conexao = sqlite3.connect("Projetodiario/banco/bandados.db")
    
    cursor = conexao.cursor()

    cursor.execute("SELECT nome FROM usuario WHERE nome=?", (criptografar(nome_usuario),))
    resultado = cursor.fetchone()

    conexao.close()

    return resultado is not None

# Função para realizar o registro do usuário
def realizar_registro(nome_usuario, senha, repetir_senha):
    conexao = sqlite3.connect("Projetodiario/banco/bandados.db")
    cursor = conexao.cursor()
    if verificar_nome_usuario(nome_usuario):
        return "Nome de usuário já em uso."
    if not verificar_senha(senha):
        return "A senha deve ter entre 6 e 10 caracteres, incluindo pelo menos uma letra maiúscula, uma letra minúscula e um número."
    if senha != repetir_senha:
        return "As senhas não coincidem."


    cursor.execute("INSERT INTO usuario (nome, senha) VALUES (?, ?)",
                   (criptografar(nome_usuario), criptografar(senha)))
    conexao.commit()

    conexao.close()

    return "Registro realizado com sucesso!"

# Interface da página de registro
def tela_registro():
    # Chama o script bandados.py para criar o banco
    subprocess.call(["python3", "Projetodiario/banco/bandados.py"])

    st.title("Registro de Usuário")
    st.write("Preencha os campos abaixo para se registrar:")

    
    # campos de entrada
    nome_usuario = st.text_input("Nome de Usuário", max_chars=20)
    senha = st.text_input("Senha", type="password", max_chars=10)


    # Verificação de senha
    st.write(f"<small>Requisitos da senha: {'Requisitos atendidos.' if len(senha) >= 6 and any(char.isdigit() for char in senha) and any(char.islower() for char in senha) and any(char.isupper() for char in senha) else ''}</small>", unsafe_allow_html=True)

    if len(senha) < 6:  # Verifica se a senha possui menos de 6 caracteres
        st.warning("A senha deve ter no mínimo 6 caracteres.")
    if not any(char.isupper() for char in senha):  # Verifica se a senha não contém nenhuma letra maiúscula
        st.warning("A senha deve conter pelo menos uma letra maiúscula.")
    if not any(char.islower() for char in senha):  # Verifica se a senha não contém nenhuma letra minúscula
        st.warning("A senha deve conter pelo menos uma letra minúscula.")
    if not any(char.isdigit() for char in senha):  # Verifica se a senha não contém nenhum número
        st.warning("A senha deve conter pelo menos um número.")

    # Campo de entrada
    repetir_senha = st.text_input("Repetir Senha", type="password", max_chars=10)

    if senha != repetir_senha:  # Verifica se as senhas não coincidem
        st.warning("As senhas não coincidem.")

    email = st.text_input("Email", max_chars=255)


    # Verificação e processamento do registro
    if st.button("Registrar"):
        if nome_usuario == "" or senha == "":
            st.error("Todos os campos devem ser preenchidos.")
        else:
            resultado = realizar_registro(nome_usuario, senha, repetir_senha)
            if resultado == "Registro realizado com sucesso!":
                st.success(resultado)
                query_string="pagina=tela_login"
            else:
                st.error(resultado)

    

# Execução da interface do Streamlit
if __name__ == "__main__":
    tela_registro()
