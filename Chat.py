import os
import openai
import streamlit as st

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")
# 创建Streamlit应用程序
st.title("ChatGPT")

# 添加一个文本输入框，以便用户输入问题
question = st.text_input("请输入您的问题")

# 添加一个“确认”按钮，以便用户提交问题
if st.button("确认"):
    # 调用OpenAI API，并传递问题作为“prompt”参数
    response = openai.Completion.create(
        engine="davinci-3", prompt=question, max_tokens=2048, n=1, stop=None, temperature=0.7,
    )
    # 获取API返回的答案
    answer = response.choices[0].text.strip()
    
    # 在Streamlit应用程序中添加一个只读文本框，以显示GPT的答案
    st.text_area("ChatGPT 的回答", value=answer, height=200, max_chars=None, key=None)
