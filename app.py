import streamlit as st

# 1. Background Color
st.markdown(
    """
    <style>
    .stApp {
        background-color: #F48FB1; /* Soft Pink  Background */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 2. Title & Cartoon Character Image
st.title("Welcome to My Fun Page! 🚀")
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNnF9zhdoqkh_p8IzgeHW3LbDhKGVWAKmCIQ3YeRZ1_STu9EZnm6T2T6Hn&s=10")

# 3. Audio / Song
st.subheader("🎵 Listen to Kyary Pamyu Pamyu - CANDY CANDY")
st.video("https://www.youtube.com/watch?v=UoK8DaJRDaM")

# 4. Interactive Questions
st.divider()

# --- Question 1 ---
c1 = st.text_input("1. What is today's date? (Format: 28th)", key="q1")

if c1:
    if "28" in c1:
        st.write("✨ Oh I heard a princess was born today!!")
    else:
        st.write("😜 Today is 28th lozer, a princess was born today")

    # --- Question 2 (only appears if Q1 is answered) ---
    c2 = st.text_input("2. Do you know the princess? I heard she is from heaven (Yes/No):", key="q2")
    
    if c2:
        if c2.strip().lower() in ["yes", "y"]:
            st.write("Me too kind of")
        else:
            st.write("How dumb can someone be")
        st.write("Well idc if uk ik her she is super cute and adorable I want to meet her one day 💕")

        # --- Question 3 (only appears if Q2 is answered) ---
        c3 = st.text_input("3. So what is ur fav cartoon character?:", key="q3")
        
        if c3:
            st.write(f"Hmmmm **{c3}** is perfect!")

            # --- Question 4 (only appears if Q3 is answered) ---
            c4 = st.text_input("4. Anyways did u get any idea who is the princess? (Yes/No):", key="q4")
            
            if c4:
                if c4.strip().lower() in ["yes", "y"]:
                    st.write("Who is it??? >_<")
                else:
                    st.write("Come on u r not so dumb, uk her, think!!!!")

                # --- Question 5 (only appears if Q4 is answered) ---
                c5 = st.text_input("5. Tell me who is the pari!!!!:", key="q5")
                
                if c5:
                    if c5.strip().lower() in ["hibbah", "hibbu", "hibbi"]:
                        st.write("🎉 Oh yaaaa!!!! the nonchalant girl I have been talking to")
                    else:
                        st.write("It is my cutie Hibbah -_-, who else can u even think about apart from her")

                    st.divider()


# 5. Submit Button
if st.button("Submit"):
    st.balloons()
    # 5. Submit Button
if st.button("Submit"):
    st.balloons()
    st.success(f"""HAPPY BIRTHDAY TO ONE OF THE MOST IMPORTANT PERSON IN MY LIFE!!!

Today is really a great day because today is the day you were born. You mean really a lot to me
Ye jo link ki jhan jhad may kara tha it was for this only :). Anyways jaysay taysay ban gaiya, but the most important thing is I was able to complete it before ur birthday.
Idk aapki kya value hay dusro ki life may but for me u matter the most, I want to see you happy ur whole life with or without me.
May Allah help you get past all the difficulties you are facing and bring lot of joy in your life
May Allah make you a successful cardiologist, may He help you in this world and akhirah
May Allah keep your eyes, your smile, your laugh, your happiness the whole you safe from shaitan and any nazar
Ameen.""")
