import streamlit as st
import numpy as np
import pandas as pd



def display():
    display_sidebar()
    display_body()


def display_sidebar():
   st.sidebar.title('choose your chart')
   charts_names=['lone_chart','other']
   choice = st.sidebar.radio('Navigation',charts_names,index=1)
   st.write('**your choice:**',choice)


def display_body():
    chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

    st.line_chart(chart_data)