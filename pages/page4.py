import streamlit as st
import numpy as np
import pandas as pd



def display():
    choice = display_sidebar()
    display_body(choice)


def display_sidebar():
   st.sidebar.title('choose your chart')
   charts_names=['line_chart','other']
   choice = st.sidebar.radio('Navigation',charts_names,index=1)
   st.write('**your choice:**',choice)
   return choice


def display_body(choice):
    if choice == 'line_chart':
        data = pd.read_csv("CSV/Streamlit_test.csv")
        line_chart_data = pd.DataFrame(data['nbcust'])
        st.line_chart(line_chart_data)
    else:
        st.write('no other chart')