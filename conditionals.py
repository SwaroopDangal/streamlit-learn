import streamlit as st
from datetime import date


st.title("Conditionals ")


add_masala = st.checkbox("Add masala?")
if add_masala:
    st.success("Masala added to your chai!")
tea_type= st.radio("Select your tea type:",["Green Tea", "Black Tea", "Herbal Tea"])
st.write(f"You selected: {tea_type}")

flavour = st.selectbox("Choose your flavour:", ["Mint", "Lemon", "Ginger"])
st.write(f"You selected: {flavour}")

sugar = st.slider("Select sugar level(spoon):", 0, 5, 2)
st.write(f"You selected: {sugar} spoon(s) of sugar")

cups = st.number_input("How many cups",min_value=1, max_value=10, step=1)
st.write(f"You selected: {cups} cup(s)")

name= st.text_input("Enter your name")
if name:
    st.write(f"Hello {name}")

dob = st.date_input("Enter your date of birth")
if dob:
    st.write(f"You entered your date of birth as {dob}")
    st.write(f"Your age is: {date.today().year - dob.year}")


if st.button("Click me"):
    st.success("Your chai is being brewed!")