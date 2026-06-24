def todo_manager():
   todo_list = []


   while True:
      print("1.  Add Task")
      print("2.  Remove task")
      print("3.  View Task")    
      print("4.  Exit")

      choice = input("Enter the Choice : ")
      if choice == '1':
         task = input("Enter the Task : ")
         todo_list.append(task)
         print(f"task {task} Added!")

      elif choice == '2':
         if not todo_list: 
            print("No tasks to Remove")

         else:
            for i,t in enumerate(todo_list,start=1):
               print(f"{i}.{t}")

            index = int(input("Enter the Task you want to remove :")) -1
            if 0 <= index < len(todo_list):
               removed = todo_list.pop(index)
               print(f"Task {removed} removed!")
            else:
               print("Invalid choice")


      elif choice == '3':
         if not todo_list:
            print("No Tasks Found")

         else:
            for i,t in enumerate(todo_list,start=1):
               print(f"{i}.{t}")

      elif choice == '4':
         print("exciting Todo list")
         break

      else:
            print("Not a valid choice,Pal")         
  


todo_manager()
          




                        

             




