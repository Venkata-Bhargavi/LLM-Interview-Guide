import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure Google API key
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the GenerativeModel with Gemini model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Define interview preparation options
options = {
    'Data Science': 'Which data science interview question would you like help with?',
    'Data Engineering': 'Which data engineering interview question would you like help with?',
    'Data Analytics': 'Which data analytics interview question would you like help with?',
    'ML Engineering': 'Which ML engineering interview question would you like help with?'
}

# Streamlit app
st.title('Interview Preparation Chatbot')

# Sidebar for navigation
page = st.sidebar.selectbox('Select a page:', ['Interview Preparation', 'Ask a Question'])

if page == 'Interview Preparation':
    # Sidebar to choose interview focus
    user_choice_role = st.sidebar.selectbox('Select Interview Focus', list(options.keys()))

    # Initialize session state for tracking button clicks
    if 'started' not in st.session_state:
        st.session_state.started = False
    if 'learning' not in st.session_state:
        st.session_state.learning = False
    if 'topics_covered_res' not in st.session_state:
        st.session_state.topics_covered_res = ""
    if 'user_topic' not in st.session_state:
        st.session_state.user_topic = ""
    if 'topic_level' not in st.session_state:
        st.session_state.level = False

    # Main app logic
    if st.button('Get Started'):
        st.session_state.started = True
        st.session_state.learning = False
        # Generate topics to be covered for the selected role
        topics_covered_res = model.generate_content(
            [
                f"What are the list of topics to be covered to crack {user_choice_role} interview?"])  # Task specific prompt pattern
        st.session_state.topics_covered_res = topics_covered_res.text

    if st.session_state.started:
        st.subheader(f'Topics to be covered for {user_choice_role} role:')
        st.write(st.session_state.topics_covered_res)

        # Prompt user to choose a specific topic to start learning
        st.subheader('Choose a specific topic to start learning:')
        user_topic = st.text_input('Type your chosen topic here:')
        st.session_state.user_topic = user_topic

        if st.button('Start Learning'):
            st.session_state.learning = True

    if st.session_state.learning and st.session_state.user_topic:
        st.subheader('Choose an Option')
        # Display radio buttons for user selection
        topic_level = st.radio('Select learning level:', ('Basics', 'Advanced Topics', 'Interview Questions'))
        if st.button('Choose Level'):
            st.session_state.level = True

        if st.session_state.level:
            if topic_level == "Interview Questions":
                # Persona prompt pattern
                interview_prompt = f"Imagine you are a {user_choice_role} interviewer, give most important and frequently asked interview questions on {st.session_state.user_topic} topics"
                response_interview = model.generate_content([interview_prompt])
                st.write(response_interview.text)
            else:
                response_prompt = f"Help me learn {st.session_state.user_topic} for {user_choice_role} interview with examples and solutions."
                response = model.generate_content([response_prompt])
                st.write(response.text)

elif page == 'Ask a Question':
    st.subheader('Ask a Question')
    question = st.text_input('What is the problem you want to solve')

    if st.button('Get Answer'):
        try:
            chain_of_thought_prompt = (
                f"Solve the following problem step-by-step:\n\n"
                f"1. Understand the Problem: Clarify what the problem is asking and summarize it.\n"
                f"2. Identify Requirements: List the key requirements or constraints needed to solve the problem.\n"
                f"3. Develop a Strategy: Outline a strategy or approach to solve the problem based on the requirements.\n"
                f"4. Detailed Solution: Provide a detailed solution using a structured approach or algorithm.\n"
                f"5. Implementation: If applicable, provide a code implementation or practical steps to achieve the solution.\n"
                f"6. Example or Demonstration: Optionally, include an example or demonstration to illustrate the solution.\n"
                f"7. Conclusion: Summarize the solution and discuss any considerations or optimizations.\n\n"
                f"{question}"
            )
            response = model.generate_content([chain_of_thought_prompt])
            st.write(response.candidates[0].content.parts[0].text)

        except Exception as e:
            st.error(f"Error generating answer: {e}")