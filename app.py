import streamlit as st
from mental_health_utils import analyze_mental_state
from css import custom_css

# Inject custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

st.title("💬 AI-Based Mental Health Support")
st.markdown("Type your thoughts or feelings, and receive support and guidance.")

user_input = st.text_area("🧠 How are you feeling today?", height=150)

if st.button("Get Support"):
    if user_input.strip() == "":
        st.warning("Please enter your thoughts or feelings.")
    else:
        label, score, recommendation = analyze_mental_state(user_input)

        if label == "negative":
            st.error(f"⚠️ Detected Emotional Tone: **{label.capitalize()}** ({round(score*100, 2)}%)")
            st.markdown(f"### 🧘 Recommendations:\n{recommendation}")
        else:
            st.success(f"✅ Detected Emotional Tone: **{label.capitalize()}** ({round(score*100, 2)}%)")
            st.markdown(f"### 🌟 Suggestions to Maintain Good Mental Health:\n{recommendation}")
