import streamlit as st
import requests
st.header("Pokemon Images")
mypokemon=['charizard','pikachu','eevee','snorlax','garchomp','lucario']
selection = st.selectbox("Select your Pokemon", mypokemon)
if selection:
    r=requests.get(f'https://pokeapi.co/api/v2/pokemon/{selection}').json()
    for img in r['sprites'].values():
        if img is not None:
            if str(img)[-4:]=='.png':
                st.image(img)
