import streamlit as st

st.set_page_config(
    page_title="Sahayak AI",
    page_icon="🤝",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: #f5f8fc;
}
.main-title {
    text-align: center;
    color: #173b67;
    font-size: 42px;
    font-weight: 800;
}
.subtitle {
    text-align: center;
    color: #52657a;
    font-size: 17px;
}
div.stButton > button {
    width: 100%;
    min-height: 75px;
    border-radius: 16px;
    font-size: 22px;
    font-weight: 700;
    border: 2px solid #245a91;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="main-title">🤝 Sahayak AI</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="subtitle">Technology for everyone</div>',
    unsafe_allow_html=True
)

st.write("")
st.write("")

st.subheader("Choose your mode")
st.write("Select the mode that suits your needs.")

if st.button("👁️  Blind Mode", use_container_width=True):
    st.session_state.mode = "blind"

if st.button("🤟  Deaf Mode", use_container_width=True):
    st.session_state.mode = "deaf"

if st.session_state.get("mode") == "blind":
    st.divider()
    st.header("👁️ Blind Mode")
    st.info("Voice assistant and object detection will be added here.")
    if st.button("⬅️ Back to Home"):
        del st.session_state.mode
        st.rerun()

elif st.session_state.get("mode") == "deaf":
    st.divider()
    st.header("🤟 Deaf Mode")
    st.info("Speech-to-text and text-to-speech will be added here.")
    if st.button("⬅️ Back to Home"):
        del st.session_state.mode
        st.rerun()

st.divider()
st.caption("Sahayak AI | Accessibility through technology")