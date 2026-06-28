import streamlit as st

st.title("📄 Skin Report")

skin = st.session_state.get("skin")

if skin is None:
    st.warning("No report available.")
    st.stop()

st.subheader("Analysis Result")

st.write("Predicted Skin Type")

st.success(skin)

st.download_button(

    "Download Report",

    data=f"Skin Type : {skin}",

    file_name="Skin_Report.txt"
)