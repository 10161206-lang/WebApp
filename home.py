# views/home.py
import streamlit as st
import backend

st.title("Potholes in Philadelphia Overview")

#test backend

numbers = backend.show_data()

st.subheader("Backend Test")
for number in numbers:
    st.write(number)

#image test
st.subheader("potholes")
st.image("assets/play.jpg", width= 300,  caption="Potholes in Philadelphia")