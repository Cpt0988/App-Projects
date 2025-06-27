import function
# 3rd party lib
import FreeSimpleGUI as gui
import time
import os


if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass
        


gui.theme('Black')


clock = gui.Text('', key = 'clock')
label=gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip = "Enter to-do", key="todo")
add_button = gui.Button("Add")
list_box = gui.Listbox(values= function.get_todos(), key='todos',
                       enable_events=True, size=[45,10])
edit_button = gui.Button("Edit")
complete_button = gui.Button("Complete")
exit_button = gui.Button("Exit")

#create a window and button
window = gui.Window('My To-Do App', 
                    layout=[[clock],
                            [label], 
                            [input_box,add_button],
                            [list_box, edit_button,complete_button],
                            [exit_button]
                            ], 
                    font=('Helvetica',15))

while True:
    # show the action of the add button and position
    event,values = window.read(timeout=10)
    window["clock"].update(value= time.strftime("%b %d,%H:%M:%S"))
    #print(event)
    #print(values)
    #print(values['todos'])
    
    match event:
        case "Add":
            todos = function.get_todos()
            new_todo = values['todo']+"\n"
            todos.append(new_todo)
            function.write_todos(todos)
            window['todos'].update(values=todos)
        
        
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
            
                todos = function.get_todos()
                index= todos.index(todo_to_edit)
                todos[index]= new_todo
                function.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                gui.popup("Please select a item first.", font=('Helvetica',15))
                
        case "Complete":
            try:
                todo_complete = values['todos'][0]
                todos = function.get_todos()
                todos.remove(todo_complete)
                function.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                gui.popup("Please select a item first.", font=('Helvetica',15))
        
        case "Exit":
            break
            
        case "todos":
            window['todo'].Update(value= values['todos'][0])
            
        # error of none that can kill your program
        case gui.WIN_CLOSED:
            break
            
        
window.close()