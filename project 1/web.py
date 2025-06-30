#lib to create web app & function
import streamlit as st
import function

todos= function.get_todos()

def add_todo():
    todo=st.session_state["new_todo"]
    todos.append(todo)
    function.write_todos(todos)

todos = function.get_todos()

st.title("My Todo App")
st.subheader("test")
st.write("This app to have you be more productive.")

for todo in todos:
    st.checkbox(todo)
    
st.text_input(label="", 
              placeholder= "Add todo..", 
              on_change= add_todo,
              key='new_todo')


#st.button(label="Submit",)