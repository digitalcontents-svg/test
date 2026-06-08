import streamlit as st
import google.generativeai as genai

# 1. पेज का डिज़ाइन
st.set_page_config(page_title="DAV Helpdesk", page_icon="🏫")
st.title("🏫 DAV School Tohana - AI Helpdesk")
st.write("Welcome! Ask any question about admissions, holidays, or timings.")

# 2. अपनी Gemini API Key यहाँ डालें
genai.configure(api_key="AQ.Ab8RN6K6Kc807o6ko1OWwkGOZo6HuYZGnW0nwI_qSy_iob6VSg")
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. AI को स्कूल की जानकारी देना (Prompt)
school_info = """
You are the polite AI Receptionist of DAV Public School, Tohana. 
Reply in short sentences in Hindi or English. 
Info: Admissions open for Class 1 to 12. Timings: 8 AM to 2 PM. 
Summer holidays: 25 May to 30 June. Principal: Mr. Sharma.
If you don't know the answer, say 'Please contact the school office.'
"""

# 4. यूज़र से सवाल लेना
user_question = st.text_input("Type your question here:")

if st.button("Ask AI"):
    if user_question:
        with st.spinner("Thinking..."):
            # AI से जवाब मांगना
            prompt = school_info + "\n\nParent asks: " + user_question
            response = model.generate_content(prompt)
            
            # जवाब स्क्रीन पर दिखाना
            st.success(response.text)
    else:
        st.warning("Please type a question first.")
