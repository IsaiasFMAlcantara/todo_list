from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, func
from sqlalchemy.orm import relationship, Session
from common.database.db import Base
from sqlalchemy.exc import SQLAlchemyError

class Todo(Base):
    __tablename__ = "todos"
    __table_args__ = {'extend_existing': True}  # Adiciona esta linha

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    status = Column(Integer, default=1)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now())

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="todos")

def add_todo(db: Session, title: str, description: str, user_id: int):
    try:
        new_todo = Todo(
            title=title,
            description=description,
            user_id=user_id
        )

        db.add(new_todo)
        db.commit()
        db.refresh(new_todo)

        return new_todo
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Erro ao adicionar o Todo: {str(e)}")
        return None

def get_todos_by_user_and_status(db: Session, user_id: int, status: int):
    try:
        todos = db.query(Todo).filter(
            Todo.user_id == user_id,
            Todo.status == status
        ).all()
        return todos
    except SQLAlchemyError as e:
        print(f"Erro ao buscar todos: {e}")
        return []