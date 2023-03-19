import openai
import streamlit as st

# 设置 OpenAI API 密钥
openai.api_key = os.getenv("OPENAI_API_KEY")

# 定义函数，根据输入的关键字和内容生成报告
def generate_report(keyword, content, length):
    prompt = f"请根据以下关键词和内容，生成市场调研报告：\n关键字：{keyword}\n内容：{content}\n报告字数：{length}\n\n报告："
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=length,
        n=1,
        stop=None,
        temperature=0.7,
    )
    report = response.choices[0].text
    return report

# Streamlit 应用程序
def app():
    # 设置页面标题
    st.title("市场调研报告生成器")

    # 接收用户输入
    keyword = st.text_input("请输入关键字：")
    content = st.text_input("请输入内容：")
    length = st.number_input("请输入报告字数：", min_value=10, max_value=10000, value=500)

    # 生成报告
    if st.button("生成报告"):
        if keyword and content:
            report = generate_report(keyword, content, length)
            st.write(report)
        else:
            st.warning("请先输入关键字和内容")

# 运行 Streamlit 应用程序
if __name__ == "__main__":
    app()
