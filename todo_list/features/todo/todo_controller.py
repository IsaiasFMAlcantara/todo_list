import streamlit as st
from todo_list.services.todo.todo_service import todo_service, todo_get_service, todo_get_id_service


def todo_controller(titulo: str, descricao: str, idusuario: int):
    if not titulo or not descricao or not idusuario:
        st.error("Por favor, preencha todos os campos antes de adicionar o Todo.")
        return

    new_todo = todo_service(title=titulo, description=descricao, user_id=idusuario)

    if new_todo:
        st.success(f'Todo "{new_todo.title}" adicionado com sucesso!')
        st.rerun()
    else:
        st.error("Não foi possível adicionar o Todo. Tente novamente.")

def todo_list_controller(status: int, idusuario: int):
    if status is None or not idusuario:
        st.error("Por favor, selecione um status e informe o ID do usuário.")
        return

    todos = todo_get_service(status=status, user_id=idusuario)

    if todos:
        return todos 
    else:
        return False
    
def todo_list_id_controller(idtask: int, idusuario: int):
    if idtask is None or not idusuario:
        st.error("Por favor, selecione um status e informe o ID do usuário.")
        return

    todos = todo_get_id_service(taskid=idtask, user_id=idusuario)

    if todos:
        return todos 
    else:
        return False

