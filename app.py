import streamlit as st
from google import genai

st.set_page_config(page_title="RAS-Guru")
st.title("RAS-Guru")
st.caption("RPSC Prelims + Mains - Jaipur Expert")

api_key = st.secrets.get("GOOGLE_API_KEY", "")
if not api_key:
    st.error("Secrets me GOOGLE_API_KEY nahi mili!")
    st.stop()

client = genai.Client(api_key=api_key)
mode = st.selectbox("Mode chuno:", ["Prelims", "Mains"])
q = st.text_area("Sawal likho:")

if st.button("Guru Ji se pucho"):
    if not q:
        st.warning("Pehle sawal likho!")
    else:
        with st.spinner("Guru Ji soch rahe hain..."):
            prompt = f"You are RAS Guru from Jaipur. Answer in Hindi. Mode {mode}. Q: {q}"
            try:
                # Latest model - Google khud suggest kar raha hai
                res = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
                st.success(res.text)
            except Exception as e1:
                try:
                    # Fallback - agar 2.5 na chale to 3.8
                    res = client.models.generate_content(model="gemini-3.8-flash", contents=prompt)
                    st.success(res.text)
                except Exception as e2:
                    st.error(f"Error 1: {e1}\n\nError 2: {e2}")
