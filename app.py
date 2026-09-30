
import streamlit as st
import google.generativeai as genai

API_KEY = "AQ.Ab8RN6L-T3YDbVNN0y0p4eF_QuuNhgEWwjhMe07n5Wu6SfNKNQ"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="RAS-Guru")
st.title("👑 RAS-Guru")
st.caption("RPSC Prelims + Mains - Jaipur Expert")

mode = st.selectbox("Mode chuno:", ["Prelims - Objective", "Mains - Answer Writing"])
q = st.text_area("Apna Sawal / Mains ka Question likho:")

if st.button("Guru Ji se pucho"):
    if not q:
        st.warning("Pehle sawal to likho!")
    else:
        if "Prelims" in mode:
            prompt = f"You are RAS-Guru. Explain this for RPSC Prelims: {q}"
        else:
            prompt = f"You are RAS Mains evaluator. Evaluate this answer: {q}"

        with st.spinner("Guru Ji soch rahe hain..."):
            try:
                res = model.generate_content(prompt)
                st.write(res.text)
            except Exception as e:
                st.error(f"Error: {e}")
