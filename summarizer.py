import os
import google.generativeai as genai

# 配置 Gemini API Key（来自环境变量）
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# 初始化 Gemini 模型（默认 gemini-pro）
model = genai.GenerativeModel("gemini-pro")

def summarize_text(text):
    prompt = f"请对下面这段Reddit内容进行简洁摘要，并指出是否存在商业潜力点：\n\n{text}"
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"[Error summarizing]: {str(e)}"
