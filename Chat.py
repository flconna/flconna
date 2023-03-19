import openai
import streamlit as st

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("简单的问答系统")

# Get user input
user_input = st.text_input("请输入您的问题：")

if user_input:
    # Call OpenAI to generate answer
    completions = openai.Completion.create(
        engine="davinci",
        prompt=user_input,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text.strip()
    
    # Show AI answer
    st.text_area("AI回答：", message, height=30, background="#f0f0f0")
