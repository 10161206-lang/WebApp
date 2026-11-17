#This is a starting template please change the comments
import streamlit as st
import backend


st.set_page_config(page_title="Potholes in Philadelphia", layout="wide")

#link views on other python scripts
home = st.Page("views/home.py", title="Home", icon="🏠", default=True)
data = st.Page("views/data.py", title="Data", icon="📊")
resources = st.Page("views/resources.py", title="Resources", icon="📚")

#navigation bar
pg = st.navigation([home, data, resources])

#run the pages
pg.run()