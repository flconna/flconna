import os
import openai
import streamlit as st

# 认证openai
openai.api_key = os.getenv("OPENAI_API_KEY")

# 设置 OpenAI 引擎的名称。
model_engine = "text-davinci-003"

# 显示聊天机器人的标题。
st.title("OpenAI 聊天机器人")

# 获取用户输入并向 OpenAI API 发送请求以获取响应。
user_input = st.text_input("您: ", "")
if user_input:
    response = openai.Completion.create(
        engine=model_engine,
        prompt=user_input,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # 提取响应中的答案文本。
    answer = response.choices[0].text.strip()

    # 将答案显示在文本区域中。
    st.text_area("机器人:", answer, height=len(answer.split("\n")), background="#f0f0f0")
