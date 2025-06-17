import os
import praw

def get_reddit_instance():
    client_id = os.getenv("APTOH3quFr6I_jo4ntjDxg")
    client_secret = os.getenv("4Rk73clDP9biN1Fi-wszS44RAhuLvA")
    user_agent = "reddit_trend_insight_app/0.1"
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         user_agent=user_agent)
    return reddit
