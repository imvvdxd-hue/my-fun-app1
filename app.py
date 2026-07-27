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

st.title("Q&A")

# 4. Interactive Questions
st.divider()

# --- Question 1 ---
c1 = st.text_input("1. What is today's date? (Format: __th)", key="q1")

if c1:
    if "28" in c1:
        st.write("✨ Oh I heard a princess was born today!!")
    else:
        st.write("Today is 28th lozer, a princess was born today")

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
            st.write(f"Hmmmm ok")

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



   # --- Submit Button (only appears after all 5 questions!) ---
                    if st.button("Submit", key="submit_btn"):
                        st.balloons()
                        st.warning(f"""HAPPY BIRTHDAY TO ONE OF THE MOST IMPORTANT PERSON IN MY LIFE!!!🥳

Today is really a great day because today is the day you were born. You really mean a lot to me.
Ye jo link ki jhan jhad may kara tha it was for this only :). Anyways jaysay taysay ban gaiya, but the most important thing is I was able to complete it before your birthday.
Idk aapki kya value hay dusro ki life may but for me you matter the most, even tho u say idc, act non chalant I still find you the most mesmerising person.\n
I want to see you happy your whole life with or without me.\n
May Allah help you get past all the difficulties you are facing and bring lot of joy in your life.
May Allah make you a successful cardiologist, May He help you in this world and akhirah.
May Allah keep your eyes,your lips, your nosy, your smile, your laugh, your happiness the whole you safe from any nazar and any thing that hurts you\n
Ameen Ameen Ameen.""")

                        # Cinnamoroll Image shows up here at the very end!
                        st.image("https://p7.itc.cn/images01/20210202/6797b5d131f14841893c52402120b08d.jpeg", caption="Happy Birthday Cinnamoroll! 🎉")

# Audio / Song (can sit outside or above)
st.subheader("Aapka fav CANDY CANDY 🎵")
st.video("https://www.youtube.com/watch?v=UoK8DaJRDaM")
