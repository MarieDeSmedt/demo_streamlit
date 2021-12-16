import streamlit as st
import streamlit as st
import numpy as np
import pandas as pd



def display():
    simple, style, table = display_sidebar()
    display_header()
    display_body(simple, style, table)
    

def display_sidebar():
    simple =st.checkbox('affichage dataframe simple', value=True)
    style =st.checkbox('affichage avec style')
    table =st.checkbox('affichage sous forme de table')
    st.sidebar.button('bouton page3')   
    return simple, style, table
    
def display_header():
    st.title("page 3")

def display_body(simple, style, table):
    dataframe = pd.DataFrame(np.random.randn(10, 20), columns=('col %d' % i for i in range(20)))
    if simple:
        st.write('affichage dataframe simple')
        st.dataframe(dataframe)
    if style:
        st.write('affichage avec style')
        st.dataframe(dataframe.style.highlight_max(axis=0))
    if table:
        st.write('affichage sous forme de table')
        st.table(dataframe)