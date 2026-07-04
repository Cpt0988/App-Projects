
# from langchain_google_genai import ChatGoogleGenerativeAI

import os
import uuid
import gradio as gr
import sqlite3

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from datetime import datetime
from langgraph.checkpoint.sqlite import SqliteSaver


load_dotenv() 

# google_api_key = os.getenv("Google_api_key")

conn = sqlite3.connect("chat_history.db",check_same_thread=False)
checkpointer = SqliteSaver(conn)

def get_date():
    """Get the current date"""
    return datetime.now().strftime("%Y-%m-%d")

# llm = ChatGoogleGenerativeAI(model ="gemini-3-flash-preview", api_key=google_api_key)
llm = ChatOllama(model="qwen2.5:3b")

# Mission statement: Create an AI agent that can answer questions and provide information to users. 
# The more information the better.
system_prompt = """
You are a helpful assistant.
Answer all user questions to the best of your ability. 
Use the get_date tool if they ask about today's date.

"""

agent = create_agent(model=llm, tools=[get_date], 
                     system_prompt=system_prompt,
                     checkpointer=checkpointer)


# user_input = input("What is your question? ")
# response = agent.invoke({"messages": [{"role": "user", "content": "Hi there!"}]})

# print(response["messages"][-1].content[0]["text"])
# print(response['messages'][-1].content)

def chat(message, history, thread_id):
    config = {"configurable" : {"thread_id": thread_id}}
    response = agent.invoke(
        {"messages": [{"role": "user", "content": message}]},
        config
    )
    last_message = response["messages"][-1].content
    return last_message

with gr.Blocks() as demo:
    gr.Markdown("## AI Agent")
    thread_id = gr.State(value = lambda: str(uuid.uuid4()))
    gr.ChatInterface(fn=chat, additional_inputs=[thread_id])
    
    
demo.launch()