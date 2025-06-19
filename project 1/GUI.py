import function
# 3rd party lib
import FreeSimpleGUI as gui

label=gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip = "Enter to-do", key="todo")
add_button = gui.Button("Add")
list_box = gui.Listbox(values= function.get_todos(), key='todos',
                       enable_events=True, size=[45,10])
edit_button = gui.Button("Edit")

#create a window and button
window = gui.Window('My To-Do App', 
                    layout=[[label], [input_box,add_button],[list_box, edit_button]], 
                    font=('Helvetica',15))

while True:
    # show the action of the add button and position
    event,values = window.read()
    print(event)
    print(values)
    #print(values['todos'])
    
    match event:
        case "Add":
            todos = function.get_todos()
            new_todo = values['todo']+"\n"
            todos.append(new_todo)
            function.write_todos(todos)
            window['todos'].update(values=todos)
        
        
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
           
            todos = function.get_todos()
            index= todos.index(todo_to_edit)
            todos[index]= new_todo
            function.write_todos(todos)
            window['todos'].update(values=todos)
        
        case "todos":
            window['todos'].Update(value= values['todos'][0])
            
        # error of none that can kill your program
        case gui.WIN_CLOSED:
            break
    
    
    
    
    
window.close()