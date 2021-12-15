
import streamlit as st

# Custom imports 
from multipage import MultiPage
from pages import page1, page2, page3

# Create an instance of the app 
app = MultiPage()



# Title of the main page
title="Test Streamlit"
title_front ="<div><span class='highlight blue'>{}</span></div>".format(title)
st.markdown(title_front, unsafe_allow_html=True)


# Add all your applications (pages) here
app.add_page("Page n°1", page1.display)
app.add_page("Page n°2", page2.display)
app.add_page("Page n°3", page3.display)


# The main app
app.run()

