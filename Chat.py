import os
import openai
import streamlit as st

# 认证openai
openai.api_key = os.getenv("OPENAI_API_KEY")
st.title("提问 by青森创造")
# 创建文本输入框
question = st.text_input("请输入您的问题")

# 创建确认按钮
if st.button("提交问题"):
    # 使用OpenAI获取答案
    answer = openai.Completion.create(
        engine="davinci",
        prompt=question,
        temperature=0.5,
        max_tokens=100,
        n=1,
        stop=None,
        timeout=5,
    )
    # 显示答案
    st.text_area(answer.choices[0].text, height=len(answer.choices[0].text.split('\n')), background='#f0f0f0')
