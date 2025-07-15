# Reddit Persona Generator

This project takes a Reddit user’s profile URL as input, scrapes their posts and comments, and uses an LLM (via LangChain + Groq API) to generate a user persona with cited sources.

## Features

- Extracts latest 20 posts and 20 comments from a Reddit user
- Uses LLM to build a structured user persona
- Each trait is **cited** with the Reddit post or comment that contributed to it
- Output saved as a `.txt` file.

---
## 🛠️ Setup Instructions

Follow the steps below to set up the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/reddit-persona-llm.git
cd reddit-persona-llm
```
### 2. Create a Virtual environment (Recommended)

```bash
python -m venv venv
```
### 3. Activate it

```bash
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```
### 3. Install Dependencies

```bash
Copy
Edit
pip install -r requirements.txt
```
### 4. Add Environment Variables
Create a .env file in the project root and add the following:
```bash
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=your_custom_user_agent
GROQ_API_KEY=your_groq_api_key
```
⚠️ Do not share or push your .env file to GitHub.

### 5. Run the Application
```bash
python main.py
```

You will be prompted to enter a Reddit profile URL (e.g. https://www.reddit.com/user/exampleuser/). 
The generated persona will be saved as a .txt file.

##  Notes

- Reddit data is fetched using **PRAW** (Python Reddit API Wrapper).
- Persona generation is powered by **LangChain** and the **Groq API**.
- The generated persona includes:
  - **Name**
  - **Age**
  - **Occupation**
  - **Education**
  - **Location**
  - **Personality traits** (with citations)
  - **Interests** (with citations)
  - **Behaviors** (with citations)
  - **Goals** (with citations)
