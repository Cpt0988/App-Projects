import function
# 3rd party lib
import FreeSimpleGUI as gui

label=gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip = "Enter to-do", key="todo")
add_button = gui.Button("Add")

#create a window and button
window = gui.Window('My To-Do App', 
                    layout=[[label], [input_box,add_button]], 
                    font=('Helvetica',15))

while True:
    # show the action of the add button and position
    event,values = window.read()
    print(event)
    print(values)
    
    match event:
        case "Add":
            todos = function.get_todos()
            new_todo = values['todo']+"\n"
            todos.append(new_todo)
            function.write_todos(todos)
        case gui.WIN_CLOSED:
            break
    
    
    
    
    
    window.close()