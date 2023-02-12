import os
import openai
import streamlit as st

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("OpenAI 文本生成 微信：青森创造")

key_info = st.text_input("输入你的关键字信息使用 '、'分隔")
length = st.slider("选择你需要生成的文章长度", min_value=1, max_value=500, value=100)

if st.button("生成文章"):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"生成一篇文章，关键信息是：{key_info}、",
        max_tokens=length,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    st.write(message)
