import streamlit as st
from google import genai
st.set_page_config(page_title="RAS-Guru", page_icon="👑")
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
            try:
                prompt = f"Tum RAS Guru ho, RPSC expert. {mode} me jawab do: {q}"
                res = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
                st.success(res.text)
            except Exception as e:
                st.error(f"Error: {e}")       
