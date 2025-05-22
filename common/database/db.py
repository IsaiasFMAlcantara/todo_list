import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager

# Base para os modelos ORM
Base = declarative_base()

# URL do banco (definida no .streamlit/secrets.toml)
DATABASE_URL: str = st.secrets["database_url"]

# Criação do engine, com suporte ao SQLite
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)

# Configuração da sessão
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Context manager para uso seguro do banco
@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
