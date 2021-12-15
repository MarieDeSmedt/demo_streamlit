
import streamlit as st

# Custom imports 
from multipage import MultiPage
from pages import page1

# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.title("Data Storyteller Application")

# Add all your applications (pages) here
app.add_page("Page n°1", page1.display)
app.add_page("Page n°2", page1.display)
app.add_page("Page n°3", page1.display)


# The main app
app.run()

