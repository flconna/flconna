import os
import openai
import streamlit as st

# 认证openai
openai.api_key = os.getenv("OPENAI_API_KEY")

# 获取 OpenAI 官方的文本生成模型 ID，这里使用了 GPT-3 的英文模型
model_engine = "text-davinci-002"

# 获取答案函数
def get_answer(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    answer = response.choices[0].text
    return answer.strip()

# 定义 Streamlit 的应用程序
def app():
    # 在 Streamlit 中创建标题
    st.title("Chatbot")

    # 在 Streamlit 中创建文本输入框，用于用户输入问题
    user_input = st.text_input("你的问题：")

    # 当用户按下回车键时，将用户输入的问题发送给 OpenAI 的文本生成模型，并获取答案
    if st.button("发送"):
        prompt = f"Q: {user_input}\nA:"
        answer = get_answer(prompt)

        # 将答案显示在 Streamlit 中的文本框中
        st.text_area("机器人:", str(answer), height=len(answer.split("\n")), background="#f0f0f0")

if __name__ == "__main__":
    app()
