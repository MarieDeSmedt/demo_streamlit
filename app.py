
import streamlit as st
#use wide mode !must be here!
st.set_page_config(layout="wide")

# Custom imports 
from multipage import MultiPage
from pages import page1, page2, page3

# Create an instance of the app 
app = MultiPage()

# Add all your applications (pages) here
app.add_page("Formule de vente", page1.display)
app.add_page("affichage dataframe/table", page3.display)
app.add_page("segmentation", page2.display)
app.add_page("", page2.display)
app.add_page("", page2.display)
app.add_page("", page3.display)
app.add_page("", page1.display)

# The main app
app.run()

