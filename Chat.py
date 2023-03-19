import os
import openai
import streamlit as st

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("问答系统")

# Get user input
user_input = st.text_input("输入你的问题：")

# Call OpenAI API to get answer
if user_input:
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_input,
        max_tokens=10,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text.strip()
else:
    message = ""

# Display AI response
st.text_area("AI回答：", message, height=30, background="#f0f0f0")
