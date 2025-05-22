from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from sqlalchemy.orm import relationship, Session
from common.database.db import Base

class User(Base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now())

    # Referência à classe como string
    todos = relationship("Todo", back_populates="user")


def buscar_por_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def inserir_usuario(db: Session, username: str, email: str, password_hash: str):

    try:
        # Cria um novo objeto User
        novo_usuario = User(
            username=username,
            email=email,
            password_hash=password_hash
        )

        # Adiciona à sessão e comita
        db.add(novo_usuario)
        db.commit()
        db.refresh(novo_usuario)  # Atualiza com o ID gerado

        print(f"Usuário criado com sucesso: {novo_usuario.id} - {novo_usuario.username}")
        return True

    except Exception as e:
        db.rollback()
        print(f"Erro ao inserir usuário: {e}")
        return False
    finally:
        db.close()