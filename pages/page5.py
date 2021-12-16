import streamlit as st
import numpy as np
import pandas as pd


def display():
    nb_points =display_slider()
    display_body(nb_points)

def display_slider():
    x = st.sidebar.slider('NB DE POINTS',5,100)  
    st.write('Nombre de points affichés',x)
    return x


def display_body(nb_points):
    map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

    st.map(map_data.head(nb_points))