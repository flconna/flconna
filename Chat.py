import os
import openai
import streamlit as st

# 认证openai
openai.api_key = os.getenv("OPENAI_API_KEY")
import openai
import streamlit as st

# 定义Streamlit页面的布局和样式
st.set_page_config(page_title="Chat with OpenAI", page_icon=":speech_balloon:")
st.title("Chat with OpenAI")
st.markdown("---")

# 定义一个函数来获取OpenAI的回答
def get_answer(prompt):
    # 调用OpenAI API来生成回答
    response = openai.Completion.create(
        engine="davinci", prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.5
    )
    # 返回回答
    return response.choices[0].text.strip()

# 在页面上创建一个文本框来获取用户的问题
question = st.text_input("Ask a question:")

# 在页面上创建一个确认按钮，当用户点击时获取OpenAI的回答
if st.button("Submit"):
    # 获取OpenAI的回答
    answer = get_answer(question)
    # 在页面上创建一个灰色背景的文本框来显示OpenAI的回答
    st.text_area(answer, height=len(answer.split('\n')), background='#f0f0f0')
