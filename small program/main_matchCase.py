
#
# help with function----dir(list)
# help(list.clear)
# sourcery skip: aug-assign, ensure-file-closed, merge-assign-and-aug-assign

while True:
    #Get user input and Strip space chars from it
    user_action = input(" Type add,show,edit, clear,done or exit: ")
    user_action = user_action.strip()
    
    match user_action:
     
     case 'add':
        todo = input("Enter a todo: ")+"\n"
        
       
        
        with open('todos.txt','r') as file:
            todos = file.readlines()
        
        todos.append(todo)
 
        with open('todos.txt','w') as file:
            file.writelines(todos)
     
     case 'show' | 'display':
        file = open('todos.txt','r')
        todos = file.readlines()
        file.close()
        
        for index, item in enumerate(todos):
            item = item.title().strip('\n')
            row = f"{index+1}.{item}"
            print(row)
     
     case 'edit':
        number = int(input("Number of the todo to edit: "))
        number = number -1
        
        with open('todos.txt','r') as file:
            file.readlines(todos)
            
        print('Here is todo existing:', todos)
        
        
        new = input ("Enter new todo:")
        todos[number]=new + '\n'
        
        with open('todos.txt','w') as file:
            file.writelines(todos)
          
    
     case 'done':
          number = int(input("Number of the todo that is done: "))
          
          
          with open('todos.txt','r') as file:
           todos= file.readlines(todos)
          index =number -1
          toremove = todos[index].strip('\n')
          gone= todos.pop(index)
          
          with open('todos.txt','w') as file:
            file.writelines(todos)
          
         # print(gone,"is remove.")
          message = f"Todo {toremove} was removed from the list"
          print(message)
         
     case 'clear':
         file = open('todos.txt','r+')
         file.truncate(0)
         file.close()
         print('List is clear.')
     
     
     case 'exit':
         file.close()
         break
     
     case _:
         print("Unknown command.")

print ("Bye!")
