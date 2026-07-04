


import os
import uuid
import gradio as gr
import sqlite3

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from datetime import datetime
from langgraph.checkpoint.sqlite import SqliteSaver
from langchain_community.tools.tavily_search import TavilySearchResults


load_dotenv() 



conn = sqlite3.connect("chat_history.db",
                       check_same_thread=False)
checkpointer = SqliteSaver(conn)
search_tool = TavilySearchResults()

def get_date():
    """Get the current date"""
    return datetime.now().strftime("%Y-%m-%d")

llm = ChatOllama(model="qwen2.5:3b")

# Mission statement: Create an AI agent that can answer questions and provide information to users. 
# The more information the better.
system_prompt = """
You are a helpful assistant.
Answer all user questions to the best of your ability. 
Use the get_date tool only when the user asks about today's date.
Use the search_tool for answering questions that require up-to-date information.


"""

agent = create_agent(model=llm,
                     tools=[get_date, search_tool], 
                     system_prompt=system_prompt,
                     checkpointer=checkpointer)




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