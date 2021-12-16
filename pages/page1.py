import streamlit as st
from PIL import Image
import load_css as css




select_perimetre= ['secteur','categorie','marché']
select_comparaison= ['secteur','categorie','marché']
    
    
def display():
    css.local_css("css/css_page1.css")
    display_sidebar()
    display_header()
    display_body()    

def display_sidebar():
    st.sidebar.button('bouton page1')  
    st.sidebar.selectbox("Périmètre d'étude",select_perimetre)
    st.sidebar.selectbox("Périmètre de comparaison",select_comparaison)
    
def display_header():
    title="Formule de vente"
    title_front ="<div><span class='highlight blue'>{}</span></div>".format(title)
    st.markdown(title_front, unsafe_allow_html=True)
    st.header("welcome to the page 1")

def display_body():

    st.text_input("Inscrire ici la variable a retrouver page map", key="map")
    
    #variables
    var = '5%'
    arrow_down = Image.open('images/arrow_down.png')

   
    
    
    #rowA
    colA1, colA2, colA3, colA4, colA5, colA6, colA7, = st.columns(7)
    colA4.markdown("chiffre", unsafe_allow_html=True)
    colA4.metric("CA", "70M", var)

    #rowB
    colB1, colB2, colB3, colB4, colB5, colB6, colB7, = st.columns(7)
    
    colB2.image(arrow_down)
    colB6.image(arrow_down)

    

    #rowC
    colC1, colC2, colC3, colC4, colC5, colC6, colC7, = st.columns(7)

    var2 = 150/2
    colC2.write("chiffre 2")
    colC2.metric("CA", "70M", var2)

    var3 = 200-450
    colC6.write("chiffre 3")
    colC6.metric("CA", "70M", var3)

    #rowD
    colD1, colD2, colD3, colD4, colD5, colD6, colD7, = st.columns(7)
    colD1.image(arrow_down)
    colD3.image(arrow_down)
    colD6.image(arrow_down)
    colD7.image(arrow_down)
    colD5.image(arrow_down)

    #rowE
    colD1, colD2, colD3, colD4, colD5, colD6, colD7, = st.columns(7)

    colD1.write("couleur inversée")
    colD1.metric(label="CA", value=4, delta=-0.5, delta_color="inverse")


    colD3.write("couleur inversée")
    colD3.metric("CA", "70M", var,"inverse")

    colD5.write("pas de couleur")
    colD5.metric(label="CA", value=4, delta=-0.5, delta_color="off")

    colD6.write("pas de couleur")
    colD6.metric("CA", "70M", var, "off")

    colD7.write("pas de couleur")
    colD7.metric("CA", "70M", var,"off")