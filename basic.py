import streamlit as st

st.title("Swaroop")
st.header("Hello World")
st.text("My first streamlit app")
st.write("This is a simple Streamlit application.")

chai = st.selectbox("Choose your favorite tea:", ["Masala Chai", "Green Tea", "Black Tea", "Herbal Tea"])
st.write(f"You selected: {chai}")