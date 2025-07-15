import praw
import os
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id = os.getenv("REDDIT_CLIENT_ID"),
    client_secret = os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent = os.getenv("REDDIT_USER_AGENT"),
)

def extract_username(url):
    if "reddit.com/user/" in url:
        return url.rstrip("/").split("/")[-1]
    return None

def fetch_user_data(username):
    user = reddit.redditor(username)
    posts = []
    comments = []

    for post in user.submissions.new(limit=20):
        posts.append({
            "title": post.title,
            "selftext": post.selftext,
            "subreddit": str(post.subreddit),
            "url":post.url,
            "created_utc": post.created_utc
        })
    
    for comment in user.comments.new(limit=20):
        comments.append({
            "body":comment.body,
            "subreddit": str(comment.subreddit),
            "created_utc":comment.created_utc,
            "link_title": comment.submission.title,
            "link_url": comment.submission.url
        })

    return {
        "username": username,
        "posts": posts,
        "comments": comments
    }

def get_user_data(profile_url):
    username = extract_username(profile_url)
    if not username:
        raise ValueError("Invalid Reddit profile URL.")
    
    data = fetch_user_data(username)

    # post_texts = [
    #     f"{p['title']}\n{p['selftext']}".strip()
    #     for p in data["posts"]
    # ]

    # comment_texts = [
    #     c["body"] for c in data["comments"]
    # ]

    return {
        "username": username,
        "posts": data["posts"],
        "comments": data["comments"]
    }

# test
# if __name__ == "__main__":
#     url = input("Enter Reddit profile URL: ")
#     username = extract_username(url)
#     if username:
#         data = fetch_user_data(username)
#         print(f"\nFetched {len(data['posts'])} posts and {len(data['comments'])} comments for u/{username}")
#     else:
#         print("Invalid Reddit URL.")