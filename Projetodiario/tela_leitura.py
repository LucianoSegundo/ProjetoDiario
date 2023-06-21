import streamlit as st

def tela_leitura():
    st.title("Entrada de Grande Bloco de Texto")

    # Caixa de texto para entrada do usuário
    texto = st.text_area("Insira seu texto aqui", height=300)

    # Exibir o texto inserido pelo usuário
    st.header("Texto Inserido:")
    st.write(texto)

if __name__ == "__main__":
    tela_leitura()
