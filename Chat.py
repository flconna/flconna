import os
import openai
import streamlit as st
import time

# Set OpenAI API endpoint and engine
openai.api_endpoint = "https://api.openai.com"
openai.api_key = os.getenv("OPENAI_API_KEY")
model_engine = "text-davinci-003"

# GPT-3 Completion function
def ask_gpt3(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()

# Define Streamlit app
def app():
    # Page title
    st.title("中文问答系统")

    # Text input for user
    user_input = st.text_input("请输入你的问题:")

    # Initialize AI response
    ai_response = ""

    # Check if user has entered text
    if user_input:
        # Display user question
        st.text_area("用户:", user_input, height=30, background="#f0f0f0")

        # Show loading message
        progress_bar = st.progress(0)
        with st.spinner('机器人正在思考中，请稍等...'):
            for i in range(100):
                time.sleep(0.02)
                progress_bar.progress(i + 1)

        # Generate AI response
        prompt = f"问题: {user_input}\n答案:"
        ai_response = ask_gpt3(prompt)

        # Display AI response
        st.text_area("机器人:", ai_response, height=len(ai_response.split("\n")), background="#f0f0f0")

# Run Streamlit app
if __name__ == "__main__":
    app()
