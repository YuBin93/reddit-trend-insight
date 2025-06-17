import openai

openai.api_key = "your_openai_api_key"

def generate_summary(posts):
    if not posts:
        return "无相关内容"
    content = "\n".join([f"- {p['title']} ({p['score']}分)" for p in posts])
    prompt = f"""
你是一位AI趋势研究分析师，请基于以下 Reddit 帖子标题，总结出3个可能的技术趋势或商机。

帖子列表：
{content}

请用中文简洁总结，不超过200字。
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"摘要生成失败：{e}"
