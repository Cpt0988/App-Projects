

# help with function----dir(list)
# help(list.clear)
# sourcery skip: aug-assign, ensure-file-closed, merge-assign-and-aug-assign

from function import get_todos, write_todos
import time


now=time.strftime ("%b %d, %Y %H:%M:%S" )
while True:
    #Get user input and Strip space chars from it
    print(f'The time is {now}')
    user_action = input(" Type add,show,edit, clear,done or exit: ")
    user_action = user_action.strip()
     
    if  user_action.startswith('add'):
        todo = user_action[4:]
             
        todos=get_todos()
        
        todos.append(todo + '\n')
 
        write_todos(todos)
    
    
    elif user_action.startswith('show'):
        
        todos=get_todos()
        
        for index, item in enumerate(todos):
            item = item.title().strip('\n')
            row = f"{index+1}.{item}"
            print(row)
     
   
    elif user_action.startswith('edit') :
        try:
            number = int(user_action[5:])
            number = number -1
            
            todos=get_todos()
                
            print('Here is todo existing:', todos)
            
            
            new = input ("Enter new todo:")
            todos[number]=new + '\n'
            
            write_todos(todos)
            
            
        except ValueError:
            print("Not valid command.")
# it start over at the beginning
            continue
            
    
    
    elif user_action.startswith('done'):
        try:
            number = int(user_action[5:])
            
            
            todos=get_todos()
            
            index =number -1
            toremove = todos[index].strip('\n')
            gone= todos.pop(index)
            
            write_todos(todos)
            
            message = f"Todo {toremove} was removed from the list"
            print(message)
        except IndexError:
            print('There is no item with that number.')
            continue
            
    
    elif user_action.startswith('clear'):
         with open('todos.txt','r+') as file:
             file.truncate(0)
             print('List is clear.')
     
     
    elif user_action.startswith('exit'):
       
         break
     
    else :
         print("Unknown command.")

print ("Bye!")
