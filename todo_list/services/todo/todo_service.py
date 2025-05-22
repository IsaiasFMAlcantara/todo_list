from models.todo import add_todo
from common.database.db import get_db


def todo_service(title: str, description: str, user_id: int):
    try:
        # Obtendo a sessão do banco de dados
        with get_db() as db:
            # Chamando a função para adicionar um novo Todo
            new_todo = add_todo(db=db, title=title, description=description, user_id=user_id)

            # Verifica se o Todo foi criado com sucesso
            if new_todo:
                print(f"Todo '{new_todo.title}' criado com sucesso! Bem-vindo(a).")
                return new_todo
            else:
                print("Não foi possível criar o Todo. Tente novamente.")
                return False
    
    except Exception as e:
        # Erro genérico, mas com mensagem mais amigável
        print(f"Erro ao tentar criar o Todo. Tente novamente mais tarde. Erro: {str(e)}")
        return False
