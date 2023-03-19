import os
import openai
import streamlit as st
import json
# 认证openai
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define a function to ask the OpenAI GPT-3 API a question
def ask_gpt3(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.5,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    answer = response.choices[0].text
    return answer.strip()

# Define the main Streamlit app
def app():
    st.set_page_config(page_title="Chat with GPT-3", page_icon=":robot_face:")
    st.title("Chat with GPT-3")
    user_input = st.text_input("You:", "")
    if user_input:
        prompt = f"User: {user_input}\nAI:"
        answer = ask_gpt3(prompt)
        st.text_area("机器人:", answer, height=len(answer.split("\n")), background_color="#f0f0f0")

# Run the app
if __name__ == "__main__":
    app()
