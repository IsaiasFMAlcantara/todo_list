import re
import streamlit as st
from passlib.context import CryptContext
from passlib.exc import UnknownHashError

pwd = CryptContext(schemes=[st.secrets["encode"]], deprecated="auto")

class Login:
    def _validar_email(self, email: str) -> dict:
        """Valida o formato do e-mail com regex."""
        padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        valido = re.match(padrao, email)
        return {
            'retorno': 'E-mail válido' if valido else 'E-mail inválido.',
            'status': bool(valido)
        }

    def _validar_senha(self, senha: str, hash_armazenado: str) -> bool:
        """Verifica se a senha informada bate com o hash armazenado."""
        try:
            return pwd.verify(senha, hash_armazenado)
        except UnknownHashError:
            return False

    def _criar_hash(self, senha: str) -> str | dict:
        """Gera um hash seguro para a senha."""
        try:
            return pwd.hash(senha)
        except Exception as e:
            return {
                'retorno': f"Erro ao criar o hash: {e}",
                'status': False
            }

    def criar_conta(self, nome: str, email: str, senha: str) -> dict:
        """Gera os dados do usuário para cadastro, incluindo hash da senha."""
        validacao_email = self._validar_email(email)
        if not validacao_email["status"]:
            return validacao_email

        hash_senha = self._criar_hash(senha)
        if isinstance(hash_senha, dict):
            return hash_senha  # Retorna erro do hash diretamente

        return {
            'nome': nome,
            'email': email,
            'senha': hash_senha
        }
    
    def login(self, hash_password, password):
        validate = self._validar_senha(password, hash_password)
        return validate