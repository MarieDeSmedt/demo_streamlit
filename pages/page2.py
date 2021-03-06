import streamlit as st
import streamlit as st
import numpy as np
import pandas as pd



def display():
    nb_rows, simple, style, table = display_sidebar()
    display_header()
    display_body(nb_rows, simple, style, table)
    

def display_sidebar():
    st.sidebar.subheader('Combien de lignes voulez vous?')
    nb_rows = st.sidebar.slider('',5,30)
    simple =st.sidebar.checkbox('affichage dataframe simple', value=True)
    style =st.sidebar.checkbox('affichage avec style')
    table =st.sidebar.checkbox('affichage sous forme de table')
    
    st.sidebar.button('bouton page3')   
    return nb_rows,simple, style, table
    
def display_header():
    st.title("page 3")

def display_body(nb_rows,simple, style, table):
    data = pd.read_csv("CSV/Streamlit_test.csv")
    dataframe = data.head(nb_rows)
    if simple:
        st.write('affichage dataframe simple')
        st.dataframe(dataframe)
    if style:
        st.write('affichage avec style')
        st.dataframe(dataframe.style.highlight_max(axis=0))
    if table:
        st.write('affichage sous forme de table')
        st.table(dataframe)