import streamlit as st 

st.markdown("## This is Streamlit App")

st.file_uploader('upload your file')

st.camera_input( 'camera opend')

st.audio_input("your voice has been recorded")

st.download_button("Download", "This is some text", file_name="file.txt")

