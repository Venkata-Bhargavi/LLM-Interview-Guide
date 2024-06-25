# LLM-Interview-Guide

## Interview Preparation Chatbot
### Overview
This Streamlit-based chatbot application assists users in preparing for interviews in various roles related to data science and engineering. It leverages the Google Generative AI model (Gemini-1.5-flash) to provide interview questions and detailed explanations based on user inputs.

**App Link**:  https://llm-interview-guide-bhargavi.streamlit.app/

### Features
**Interview Preparation Page:** Allows users to select a role (Data Science, Data Engineering, Data Analytics, ML Engineering) and receive a list of topics to cover for interview preparation.

**Learning Mode:** Users can choose a specific topic and learning level (Basics, Advanced Topics, Interview Questions) to get detailed explanations and interview questions generated by the AI model.

**Ask a Question Page:** Users can input a problem statement or question, and the chatbot generates a step-by-step solution using a predefined chain of thought pattern.

### Setup Instructions
#### Prerequisites
- Python 3.x
p- ip
#### Installation
1. **Clone the Repository**

```bash
git clone https://github.com/Venkata-Bhargavi/LLM-Interview-Guide.git
```
   

#### Install Dependencies

```bash
pip install -r requirements.txt
```

#### Set Environment Variables

Create a `.env` file in the root directory and add your Google API key:

`GOOGLE_API_KEY=your_google_api_key_here`

#### Running the Application
#### Run the Application

Execute the Streamlit app using:

`streamlit run app.py`

This will launch a local server. Open your browser and go to http://localhost:8501 to view the application.


#### Prompt Patterns Used

#### Task-Specific Prompt Pattern

Example: "What are the list of topics to be covered to crack {user_choice_role} interview?"

#### Persona Prompt Pattern

Example: "Imagine you are a {user_choice_role} interviewer, give most important and frequently asked interview questions on {user_topic} topics"

#### Chain of Thought Prompt Pattern

Example:

Solve the following problem step-by-step:

1. Understand the Problem: Clarify what the problem is asking and summarize it.
2. Identify Requirements: List the key requirements or constraints needed to solve the problem.
3. Develop a Strategy: Outline a strategy or approach to solve the problem based on the requirements.
4. Detailed Solution: Provide a detailed solution using a structured approach or algorithm.
5. Implementation: If applicable, provide a code implementation or practical steps to achieve the solution.
6. Example or Demonstration: Optionally, include an example or demonstration to illustrate the solution.
7. Conclusion: Summarize the solution and discuss any considerations or optimizations.



#### Usage Instructions

#### Interview Preparation

- Select a role from the sidebar.
- Click "Get Started" to receive a list of topics related to the selected role.
- Choose a specific topic and learning level to view detailed explanations and interview questions.

#### Ask a Question

- Navigate to the "Ask a Question" page.
- Enter the problem statement or question in the text input.
- Click "Get Answer" to receive a step-by-step solution generated by the chatbot.

#### Notes

- Ensure your Google API key is valid and has access to the Generative AI service.
- Customize the prompt patterns or add additional functionalities as per specific requirements.

#### Troubleshooting

- If encountering errors related to response handling or API connectivity, check your network connection and API key configuration.
- For issues specific to Streamlit or Python dependencies, refer to their respective documentation and community support.
