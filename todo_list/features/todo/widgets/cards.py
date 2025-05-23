from streamlit_card import card
import streamlit as st

def colorcard(number):
    if number == 1:
        return '#f8d7da'
    elif number == 2:
        return '#d1ecf1'
    elif number == 3:
        return '#fff3cd'
    elif number == 4:
        return '#d4edda'
    else:
        return '#000000'

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
