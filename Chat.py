import os
import openai
import streamlit as st

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")
# 设置OpenAI模型
model_engine = "text-davinci-002"

# 添加文本输入框
user_input = st.text_area("请输入您的文本：", height=200)

# 添加确认按钮
if st.button("确认"):
    # 发送请求到OpenAI API
    response = openai.Completion.create(
        engine=model_engine,
        prompt=user_input,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    # 从API响应中获取结果
    result = response.choices[0].text
    
    # 将结果输出到下方的文本框
    st.write("OpenAI API的回答：")
    st.write(result)
