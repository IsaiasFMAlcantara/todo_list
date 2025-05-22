import streamlit as st

def sidebarFunction():
    with st.sidebar:
        if "user" not in st.session_state and not st.session_state:
            st.warning("Informações do usuário não encontradas.")
        
        st.markdown("## Informações do Usuário")
        nome = st.session_state['user']['name']
        email = st.session_state['user']['email']
        st.write(f"**Nome:** {nome}")
        st.write(f"**E-mail:** {email}")
        if st.button(label='Deslogar'):
            st.logout()
            st.rerun()

def todo():
    if "user" not in st.session_state and not st.session_state:
        st.warning("Informações do usuário não encontradas.")    
    sidebarFunction()
    st.markdown("""
    <style>
        .main .block-container {
            max-width: 1200px; /* Você pode aumentar esse valor */
            padding-left: 2rem;
            padding-right: 2rem;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('# Lista de tarefas')
    col1,col2,col3,col4 = st.columns(4)
    with col1.container(border=True):
        st.error("A Fazer")

    with col2.container(border=True):
        st.info("Fazendo")

    with col3.container(border=True):
        st.warning("Pausada")

    with col4.container(border=True):
        st.success("Finalizada")

todo()