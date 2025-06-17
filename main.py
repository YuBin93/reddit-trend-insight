import os
import streamlit as st
from reddit_config import get_reddit_instance
from summarizer import generate_summary

def fetch_reddit_posts(subreddit_name="technology", limit=20):
    reddit = get_reddit_instance()
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    for submission in subreddit.hot(limit=limit):
        posts.append({
            "title": submission.title,
            "score": submission.score,
            "url": submission.url
        })
    return posts

def main():
    st.title("Reddit 趋势洞察与商机挖掘系统（MVP）")
    st.write("自动抓取 Reddit 技术版块热点帖子，结合 Gemini AI 生成趋势摘要。")

    subreddit_name = st.text_input("请输入要抓取的 Reddit 版块名称", value="technology")
    limit = st.slider("抓取帖子数量", min_value=5, max_value=50, value=20)

    if st.button("开始抓取与分析"):
        with st.spinner("抓取中..."):
            posts = fetch_reddit_posts(subreddit_name, limit)
            if not posts:
                st.warning("未抓取到任何帖子，请检查版块名称或稍后重试。")
                return
            st.subheader("抓取到的帖子")
            for i, p in enumerate(posts, 1):
                st.markdown(f"{i}. [{p['title']}]({p['url']}) (👍 {p['score']})")

        with st.spinner("生成趋势摘要中..."):
            summary = generate_summary(posts)
            st.subheader("AI 生成的趋势摘要")
            st.write(summary)

if __name__ == "__main__":
    main()
