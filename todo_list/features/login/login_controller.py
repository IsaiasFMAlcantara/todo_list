import streamlit as st
from todo_list.services.login.login_service import login_service, criar_conta_service


def login_controller(email: str, senha: str):
    usuario = login_service(email, senha)
    
    if usuario:
        st.session_state['user'] = usuario
        st.rerun()


def criar_conta_controller(nome: str, email: str, senha: str):
    novo_usuario = criar_conta_service(email, senha, nome)

    if novo_usuario:
        st.success("Conta criada com sucesso! Você já pode fazer login.")
        # Você pode armazenar o usuário e redirecionar se quiser
        # st.session_state['user'] = novo_usuario
        # st.rerun()
