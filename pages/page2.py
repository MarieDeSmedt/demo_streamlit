import streamlit as st
import load_css as css
import pandas as pd

css.local_css("css/css_page2.css")

#def variables
select_perimetre= ['secteur','categorie','marché']
select_comparaison= ['secteur','categorie','marché']

def display():
    display_sidebar()
    display_header()
    display_body()
    

def display_sidebar():
    st.sidebar.button('bouton page2')   
    st.sidebar.selectbox("Périmètre d'étude",select_perimetre)
    st.sidebar.selectbox("Périmètre de comparaison",select_comparaison)

def display_header():
    st.title("page 2")

def display_body():
    st.markdown("welcome to the page 2", unsafe_allow_html=True)

    data = pd.read_csv("CSV/Streamlit_test.csv")

    # Create a list of possible values and multiselect menu with them in it.
    PERSONAE = data['personaeSegmentLabel'].unique()
    PERSONAE_SELECTED = st.multiselect('Select segmentation', PERSONAE,default=PERSONAE)

    # Mask to filter dataframe
    mask_personae = data['personaeSegmentLabel'].isin(PERSONAE_SELECTED)

    data = data[mask_personae]
    st.table(data)
