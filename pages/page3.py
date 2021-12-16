import streamlit as st

def display():
    display_sidebar()
    display_header()
    display_body()
    

def display_sidebar():
    st.sidebar.button('bouton page3')   
    
def display_header():
    st.title("page 3")

def display_body():
    st.write ("welcome to the page 3")