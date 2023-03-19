import os
import openai
import streamlit as st
from PIL import Image

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")
# 设置OpenAI模型
model_engine = "text-davinci-003"

# 添加Logo图片
logo = Image.open("LOGO.png")
st.image(logo, use_column_width=False, width=100)

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
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.write("<h3 style='text-align: center;'>OpenAI API的回答：</h3>", unsafe_allow_html=True)
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.write(f"<div style='font-size: 20px;'>{result}</div>", unsafe_allow_html=True)
