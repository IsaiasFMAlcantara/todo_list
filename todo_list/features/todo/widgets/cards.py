from streamlit_card import card
import streamlit as st

def colorcard(number):
    return {
        1: '#f8d7da',
        2: '#d1ecf1',
        3: '#fff3cd',
        4: '#d4edda',
    }.get(number, '#000000')

def render_cards(items):
    if not items:
        st.warning('Vazio')
        return

    for item in items:
        card(
            title=item.title,
            text=item.description,
            styles={
                "card": {
                    "padding": "0",
                    "margin": "0",
                    "border": "none",
                    "box-shadow": "none",
                    "background-color": colorcard(item.status)
                },
                "title": {
                    "padding": "none",
                    "margin": "none",
                    "color": "white",
                    "font-size": "16px"
                },
                "text": {
                    "padding": "none",
                    "margin": "none",
                    "color": "white",
                    "font-size": "12px"
                },
                "image": {
                    "border": "none",
                    "border-radius": "none",
                    "margin": "none",
                    "padding": "none"
                }
            }
        )
