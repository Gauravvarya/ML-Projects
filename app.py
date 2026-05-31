import streamlit as st
st.title("Spam Detection App")
message = st.text_input("Enter a message to classify:")
if st.button("Classify"):
    if message:
        spam_words = ["free", "win", "winner", "cash", "prize", "urgent", "offer", "money", "credit", "loan"]
        # Call the spam detection function from main.py
        is_spam = any(word in message.lower() for word in spam_words)
        if is_spam:
            st.error("This message is classified as spam!")
        else:
            st.success("This message is not classified as spam.")