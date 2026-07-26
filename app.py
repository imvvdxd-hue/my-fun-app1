import streamlit as st

# 1. Background Color
st.markdown(
    """
    <style>
    .stApp {
        background-color: #fce4ec; /* Soft Pink  Background */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 2. Title & Cartoon Character Image
st.title("Welcome to My Fun Page! 🚀")
st.image("cinnamoroll.png")

# 3. Audio / Song
st.subheader("🎵 Listen to Kyary Pamyu Pamyu - CANDY CANDY")
st.video("https://www.youtube.com/watch?v=UoK8DaJRDaM")
# 4. Interactive Questions
st.divider()
name = st.text_input("What is your name?")
favorite_color = st.selectbox("Pick your favorite color:", ["Red", "Blue", "Green", "Yellow","White"])

# 5. Submit Button
if st.button("Submit"):
    st.balloons()
    st.success(f"Awesome job {name}! You picked {favorite_color}.")
