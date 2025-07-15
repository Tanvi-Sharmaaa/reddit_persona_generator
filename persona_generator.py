import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

#intialize llm
llm = ChatGroq(model="llama-3.1-8b-instant")

#define prompt template
prompt =ChatPromptTemplate.from_template("""
You are an expert AI analyst. Based on the following Reddit posts and comments, generate a detailed user persona.

For each **trait or interest**, also include **citations** as seperated indented line in the form :
> Source: "text snippet..." — from a Reddit post or comment.

Here is the content:
---------------------
Posts:
{posts}

Comments:
{comments}

Your output should include:
- Name (fictional if not available)
- Age range
- Occupation
- Education
- Location (if inferable)
- Personality traits (with citations)
- Interests (with citations)
- Behavior patterns (with citations)
- Goals (with citations)

Be concise but insightful.
""")

#combine prompt and llm into chain
chain = prompt | llm

def generate_persona(posts,comments):
    post_texts = [post['title'] + " — " + post.get('selftext', '') for post in posts]
    comment_texts = [comment['body'] for comment in comments]
    # Run the LLM chain
    return chain.invoke({
        "posts": "\n\n".join(post_texts),
        "comments": "\n\n".join(comment_texts)
    })