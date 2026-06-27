import streamlit as st


st.header("GOAT PICKER")
st.subheader("Pick your goat")

col1,col2 = st.columns(2)

with col1:
    st.header("Cristiano Ronaldo")
    st.image("https://pbs.twimg.com/media/Gr5wN06XQAAQwIj.jpg",width=200)
    vote1 = st.button("Vote for Ronaldo")

with col2:
    st.header("Lionel Messi")
    st.image("https://www.vedantu.com/seo/content-images/a2de1c30-d35c-40f2-8bbf-1c8905273394_compressed_2.jpg",width=200)
    vote2 = st.button("Vote for Messi")

if vote1:
    st.success("You voted for Ronaldo")
elif vote2:
    st.success("You voted for Messi")

name = st.sidebar.text_input("Enter your name")
goat = st.sidebar.selectbox("Select your favorite goat", ["Cristiano Ronaldo", "Lionel Messi"])

st.write(f"Hello {name}, your favorite goat is {goat}.")

with st.expander("More info"):
    st.write("This is some extra information about the goat.")
    st.write("It can be long so it can scroll.")
    st.write("You can also click on the expander to see more info.")
    st.write("You can also click on the expander to see more info.")
    