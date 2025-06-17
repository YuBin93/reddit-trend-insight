import os
import requests

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = "https://api.gemini.ai/v1/chat/completions"  # 假设API地址

def generate_summary(posts):
    if not posts:
        return "无相关内容。"
    content = "\n".join([f"- {p['title']}（评分：{p['score']}）" for p in posts])
    prompt = f"""
你是一位AI趋势研究分析师，请基于以下 Reddit 帖子标题，总结出3个可能的技术趋势或商机。

帖子列表：
{content}

请用中文简洁总结，不超过200字。
"""
    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "gemini-1",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 300,
        "temperature": 0.7,
    }
    try:
        response = requests.post(GEMINI_API_URL, headers=headers, json=data)
        response.raise_for_status()
        res_json = response.json()
        summary_text = res_json["choices"][0]["message"]["content"].strip()
        return summary_text
    except Exception as e:
        return f"摘要生成失败：{e}"
