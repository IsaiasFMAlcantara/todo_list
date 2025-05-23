from models.todo import add_todo, get_todos_by_user_and_status, get_todos_by_user_and_id
from common.database.db import get_db


def todo_service(title: str, description: str, user_id: int):
    try:
        # Obtendo a sessão do banco de dados
        with get_db() as db:
            # Chamando a função para adicionar um novo Todo
            new_todo = add_todo(db=db, title=title, description=description, user_id=user_id)

            # Verifica se o Todo foi criado com sucesso
            if new_todo:
                return new_todo
            else:
                print("Não foi possível criar o Todo. Tente novamente.")
                return False
    
    except Exception as e:
        # Erro genérico, mas com mensagem mais amigável
        print(f"Erro ao tentar criar o Todo. Tente novamente mais tarde. Erro: {str(e)}")
        return False

def todo_get_service(status: int, user_id: int):
    try:
        with get_db() as db:
            todos = get_todos_by_user_and_status(db=db, user_id=user_id, status=status)

            if todos:
                return todos
            else:
                print(f"Nenhum todo encontrado para o usuário {user_id} com status {status}.")
                return []
    
    except Exception as e:
        print(f"Erro ao buscar todos. Detalhes: {str(e)}")
        return []


def todo_get_id_service(taskid: int, user_id: int):
    try:
        with get_db() as db:
            todos = get_todos_by_user_and_id(db=db,user_id=user_id,idtask=taskid)

            if todos:
                return todos
            else:
                print(f"Nenhum todo encontrado para o usuário {user_id} com status {taskid}.")
                return []
    
    except Exception as e:
        print(f"Erro ao buscar todos. Detalhes: {str(e)}")
        return []