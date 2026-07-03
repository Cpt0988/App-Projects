import requests
import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from send_email import send_email

load_dotenv()
News_api_key = os.getenv("NEWS_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY")

url = (
    "https://newsapi.org/v2/top-headlines?"
    "category=business&"
    "language=en&"
    "pageSize=8&"
    "sortBy=publishedAt&apiKey=" + News_api_key
)

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
articles = content["articles"]
print(articles)

# AI summarizing the news
model = init_chat_model(model="gemini-3-flash-preview",
                        model_provider="google-genai",
                        api_key=google_api_key
                        )

prompt = f"""
You a news summarizer.
Write a short paragraph analyzing the news.
Add another paragraph to tell me how they affect the stock market.
Here are the news articles:
{articles} 
"""
response = model.invoke(prompt )
response_text = response.content[0]['text']
print(response_text)

body = "Subject: Daily News Summary\n\n" + response_text+"\n\n"
body = body.encode("utf-8")
send_email(message=body)