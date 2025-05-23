import streamlit as st
from streamlit_autorefresh import st_autorefresh
from todo_list.features.todo.widgets.cards import render_cards
from todo_list.features.todo.todo_controller import todo_controller,todo_list_controller

@st.dialog("Criar tarefa")
def vote():
    titulo = st.text_input(
                'Titulo', placeholder='Titulo da tarefa', label_visibility='hidden'
            )
    descricao = st.text_input(
                'Descricao', placeholder='Descrição da tarefa', label_visibility='hidden'
            )
    if st.button("Submit"):
        todo_controller(titulo,descricao,st.session_state['user']['id'])
        st.success('Tarefa adicionada com sucesso',icon="✅")
        st.rerun()

def todo():
    if "user" not in st.session_state and not st.session_state:
        st.warning("Informações do usuário não encontradas.",icon="⚠️")
  
    st_autorefresh(interval=600000, key="refresh")
    colu1,colu2 = st.columns(2)
    nome = st.session_state['user']['name']
    email = st.session_state['user']['email']
    
    with colu1:
        st.write(f"**Nome:** {nome}")
    
    with colu2:
        st.write(f"**E-mail:** {email}")
    
    st.markdown("""
    <style>
        .main .block-container {
            max-width: 1200px; /* Você pode aumentar esse valor */
            padding-left: 2rem;
            padding-right: 2rem;
        }
    </style>
    """, unsafe_allow_html=True)

    if st.button("Criar Tarefa"):
        vote()

    afazer = todo_list_controller(1,st.session_state['user']['id'])
    fazendo = todo_list_controller(2,st.session_state['user']['id'])
    pausada = todo_list_controller(3,st.session_state['user']['id'])
    finalizada = todo_list_controller(4,st.session_state['user']['id'])

    st.markdown('# Lista de tarefas')

    col1,col2,col3,col4 = st.columns(4)
    with col1.container(border=True):
        st.error("A Fazer")
        render_cards(afazer)

    with col2.container(border=True):
        st.info("Fazendo")
        render_cards(fazendo)

    with col3.container(border=True):
        st.warning("Pausada")
        render_cards(pausada)

    with col4.container(border=True):
        st.success("Finalizada")
        render_cards(finalizada)

todo()