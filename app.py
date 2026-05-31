import streamlit as st
st.title("Spam Detection App")
message = st.text_input("Enter a message to classify:")
if st.button("Classify"):
    if message:
        # Call the spam detection function from main.py
        st.success("Message classified successfully!")