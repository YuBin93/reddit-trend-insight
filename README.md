# Reddit 趋势洞察与商机挖掘系统（MVP）

基于 Reddit 热门帖子自动抓取与 Gemini AI 智能摘要，帮助快速发现技术趋势与商机。

## 功能
- 自动抓取指定 Reddit 版块热点帖子
- 结合 Gemini API 生成趋势摘要
- Streamlit 页面交互展示，方便快速迭代和验证

## 依赖
- Python 3.8+
- praw
- requests
- streamlit

## 环境变量配置

| 变量名             | 说明                   |
|--------------------|------------------------|
| `GEMINI_API_KEY`     | 你的 Gemini API Key    |
| `REDDIT_CLIENT_ID`   | Reddit 应用客户端 ID   |
| `REDDIT_CLIENT_SECRET`| Reddit 应用客户端 Secret|

## 快速部署步骤

1. 克隆仓库：

```bash
git clone https://github.com/yourrepo/reddit-trend-insight.git
cd reddit-trend-insight

2.	创建并激活 Python 虚拟环境：

python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3.	安装依赖：

pip install -r requirements.txt

4.	设置环境变量：

export GEMINI_API_KEY="你的_gemini_api_key"
export REDDIT_CLIENT_ID="你的_reddit_client_id"
export REDDIT_CLIENT_SECRET="你的_reddit_client_secret"

5.	运行项目：

streamlit run main.py

6.	浏览器打开 http://localhost:8501 即可使用

注意事项
	•	Gemini API Key 需提前申请并启用
	•	Reddit API 需要注册开发者账号，创建应用以获得 Client ID 和 Secret
	•	当前为 MVP 版本，后续会迭代优化数据抓取和模型调用策略
