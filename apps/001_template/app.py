import streamlit as st

name = st.text_input("Whaaat's yoaaaaur name?")

if name:
    st.write(f'Hello {name}!')