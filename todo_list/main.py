import streamlit as st
from todo_list.features.login.login import login
from common.database.db import Base
from common.database.db import engine

st.set_page_config(
    page_title='To-Do-List',page_icon="📝", layout='centered'
)

Base.metadata.create_all(bind=engine)

if 'user' not in st.session_state:
    login()

else:
    navigation = st.navigation(
        {
        'Páginas': [st.Page('features/todo/todo.py',title='To-Do-List')]
        }
    )
    
    navigation.run()