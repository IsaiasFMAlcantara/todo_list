import streamlit as st
from models.user import buscar_por_email, inserir_usuario
from common.database.db import get_db
from common.security.login_conf import Login


def login_service(email: str, senha: str):
    login = Login()

    try:
        with get_db() as db:
            user = buscar_por_email(db, email)

            if not user:
                print("Usuário não encontrado.")
                return False

            if login._validar_senha(senha, user.password_hash):
                informacoes = {
                    "id":user.id,
                    "email":user.email,
                    "name":user.username
                }
                return informacoes
            else:
                print("Senha incorreta.")
                return False
    
    except Exception as e:
        st.error(f"Erro ao tentar fazer login. Tente novamente mais tarde. {e}")


def criar_conta_service(email: str, senha: str, nome: str):
    login = Login()

    try:
        with get_db() as db:
            # Verifica se já existe um usuário com o mesmo e-mail
            if buscar_por_email(db, email):
                st.warning("Já existe um usuário com esse e-mail.")
                return

            conta = login.criar_conta(nome,email,senha)
            # Insere o novo usuário
            novo_usuario = inserir_usuario(db, conta['nome'], conta['email'], conta['senha'])

            if novo_usuario:
                print(f"Conta criada com sucesso! Bem-vindo(a), {novo_usuario}.")
                return novo_usuario

            else:
                print("Não foi possível criar o usuário. Tente novamente.")
                return False
    
    except Exception as e:
        print(f"Erro ao tentar criar conta. Tente novamente mais tarde. {e}")