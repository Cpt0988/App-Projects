
import os
from dotenv import load_dotenv
from langchain.agents import create_agent
# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from datetime import datetime
load_dotenv() 

# google_api_key = os.getenv("Google_api_key")


def get_date():
    """Get the current date"""
    return datetime.now().strftime("%Y-%m-%d")

# llm = ChatGoogleGenerativeAI(model ="gemini-3-flash-preview", api_key=google_api_key)
llm = ChatOllama(model="qwen2.5:3b")

# Mission statement: Create an AI agent that can answer questions and provide information to users. 
# The more information the better.
system_prompt = """
You are a helpful assistant that can answer questions and provide information.


"""

agent = create_agent(model=llm, tools=[get_date], system_prompt=system_prompt)
user_input = input("What is your question? ")
response = agent.invoke({"messages": [{"role": "user", "content": user_input}]})

# print(response["messages"][-1].content[0]["text"])
print(response['messages'][-1].content)