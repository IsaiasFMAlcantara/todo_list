import streamlit as st
from todo_list.features.login.login_controller import login_controller, criar_conta_controller


def login():
    center = st.columns([3, 4, 3])
    with center[1]:
        st.markdown('# TO-DO-LIST')
        aba_1, aba_2 = st.tabs(['Sign-in','Sign-up'])
        with aba_1:
            with st.form(key='signin'):    
                
                email = st.text_input(
                    'E-mail', placeholder='E-mail', label_visibility='hidden'
                )
                password = st.text_input(
                    'Senha',
                    placeholder='Senha',
                    label_visibility='collapsed',
                    type='password',
                )

                confirm = st.form_submit_button(label='Entrar')

                if confirm:
                    login_controller(email,password)
        
        with aba_2:
            with st.form(key='signup'):    
                name = st.text_input(
                    'Nome', placeholder='Nome', label_visibility='hidden'
                )
                email = st.text_input(
                    'E-mail', placeholder='E-mail', label_visibility='collapsed'
                )
                password = st.text_input(
                    'Senha',
                    placeholder='Senha',
                    label_visibility='collapsed',
                    type='password',
                )

                confirm = st.form_submit_button(label='Inscrever-se')
                if confirm:
                    criar_conta_controller(name,email,password)