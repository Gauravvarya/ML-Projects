import streamlit as st
#Load css
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
#Title of the app
st.markdown("<h1>📩Spam Message Classifier</h1>",unsafe_allow_html = True)
#subtitle
st.markdown("<p class='Subtitle'>check whether a message is spam or not using machine learning</p>", unsafe_allow_html=True)
message = st.text_area("✉️Enter your message:", placeholder="Type your message here...")
if st.button("Classify"):
    if message:
        spam_words = ["free", "win", "winner", "cash", "prize", "urgent", "offer", "money", "credit", "loan"]
        # Call the spam detection function from main.py
        is_spam = any(word in message.lower() for word in spam_words)
        
        if is_spam:
            st.error("⚠️This message is classified as spam!")
        else:
            st.success("✅This message is not classified as spam.")

st.markdown("""
<div class="card-container">
<div class="card purple-card">
<h3>⚡️fast Prediction</h3>
<p>Instant spam detection results</p>
</div>

<div class="card blue-card">
<h3>🧠 Machine Learning</h3>
<p>Powered by Naive Bayes Algorithm</p>
</div>

<div class="card green-card">
<h3>🔒secure</h3>
<p>Your data is safe with us</p>

</div>  
</div>                      
""", unsafe_allow_html=True)   

st.markdown("""<div class ="spam box">🚫Spam message detected</div>""", unsafe_allow_html=True)        
st.markdown("<p class='Footer'>Copyright © 2023 Spam Message Classifier. All rights reserved.</p>", unsafe_allow_html=True)