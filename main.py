import modules

while True:
    print("1. Add task")
    print("2. mark task done")
    print("3. lists task")
    print("4. exit")

    choice = input("enter the choice :")

    if choice == '1':
        desc = input("enter task :")
        modules.add_task(desc)

    elif choice == '2':
        index = int(input("Enter task index to mark done:"))
        modules.mark_task_done(index)    

    elif choice =='3':
        modules.list_tasks()

    elif choice == '4':
        break
    else:
        print("invalid choice")        