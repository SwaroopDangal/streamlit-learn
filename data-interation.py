import streamlit as st
import pandas as pd

st.title("Chai Sales Dashboard")

file = st.file_uploader("Upload your sales data (CSV)", type=["csv"])
if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)

if file:
    st.subheader("Summary")
    st.write(df.describe())

if file:
    cities = df['City'].unique()
    selected_city = st.selectbox("Select your city", cities)
    filtered = df[df['City'] == selected_city]
    st.dataframe(filtered)
