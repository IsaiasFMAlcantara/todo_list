from streamlit_card import card
import streamlit as st

def render_cards(items):
    if not items:
        return st.warning('Vazio')

    for item in items:
        card(
            title=item.title,
            text=item.description
        )
