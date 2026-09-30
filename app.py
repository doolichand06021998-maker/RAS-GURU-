import streamlit as st
from google import genai

st.set_page_config(page_title="RAS-Guru")
st.title("RAS-Guru")
st.caption("RPSC Prelims + Mains - Jaipur Expert")

api_key = st.secrets.get("GOOGLE_API_KEY", "")
if not api_key:
    st.error("Secrets me Key nahi mili!")
    st.stop()

client = genai.Client(api_key=api_key)
mode = st.selectbox("Mode chuno:", ["Prelims", "Mains"])
q = st.text_area("Sawal likho:")

if st.button("Guru Ji se pucho"):
    if not q:
        st.warning("Pehle sawal likho!")
    else:
        with st.spinner("Soch rahe hain..."):
            prompt = f"You are RAS Guru. Mode {mode}. Q: {q}. Hindi me jawab do."
            res = client.models.generate_content(model="gemini-1.5-flash", contents=prompt)
            st.success(res.text)
