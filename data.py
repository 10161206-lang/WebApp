# views/data.py
import streamlit as st
import backend



st.title("Philadelphia Potholes Analytics")

st.subheader("Analysis of Potholes in Philadelphia")

data = backend.create_df("data/pothole.csv")

st.bar_chart(data, x="zipcode", y="count", sort="count")

