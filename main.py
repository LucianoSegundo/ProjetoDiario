import streamlit as st
import subprocess
from tela_registro import tela_registro
from tela_leitura import tela_leitura
from tela_escrita import tela_escrita


def main():
    subprocess.call(["python3", "banco/bandados.py"])

    st.title("Projedifun, seu diário 100% funcional")

    # Criando a barra lateral para a navegação
    st.sidebar.title("Menu de Navegação")
    pagina = st.sidebar.radio("Selecione uma página",
                              ("Registro", "Escrita", "Leitura"))

    # Exibindo a página selecionada
    if pagina == "Registro":
        tela_registro()
    elif pagina == "Leitura":
        tela_leitura()
    elif pagina == "Escrita":
        tela_escrita()


if __name__ == "__main__":
    main()
