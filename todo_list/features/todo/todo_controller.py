import streamlit as st
from todo_list.services.todo.todo_service import todo_service


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
