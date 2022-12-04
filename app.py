import streamlit as st


st.title("Cars Rating Prediction")

nav = st.sidebar.radio("Navigation",["Home","Prediction","Contribute"])


if nav == "Home":
    st.write("Home")

if nav == "Prediction":
    st.write("Prediction")

if nav == "Contribution":
    st.write("Contri")