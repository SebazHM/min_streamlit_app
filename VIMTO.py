import datetime

import streamlit as st

st.title("Min första Streamlit-app")
st.header("Välkommen!")
st.subheader("Här lär vi oss Streamlit")

if st.button("Klicka här!"):
    st.write("Du klickade på knappen!")

namn = st.text_input("Vad heter du?")
if namn:
    st.write(f"Hej, {namn}! Välkommen till Stremlit.")

print (datetime.date.today())
st.write(datetime.date.today())
