import os
import openai
import streamlit as st

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")
# 设置OpenAI模型
model_engine = "text-davinci-002"

# 设置网页标题和宽度
st.set_page_config(page_title="文本模型问答", page_icon=":pencil2:", layout="wide")

# 添加页面标题
st.title("OpenAI文本模型问答")

# 添加文本输入框
with st.form(key="text_input_form"):
    st.write("请输入您的文本：")
    user_input = st.text_area("", height=200, key="user_input")
    # 添加确认按钮
    submitted = st.form_submit_button("确认")

# 处理确认按钮提交的事件
if submitted:
    if user_input:
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
    else:
        st.warning("请输入您的问题！")
