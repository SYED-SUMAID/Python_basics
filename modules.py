tasks = []
def add_task(task):
    tasks.append({"task" :task, "done" :False})

def mark_task_done(index):
    if 0<= index < len(tasks):
        tasks[index]["done"] = True
    else:
        print("invalid index")     

def list_tasks():
    if not tasks:
        print("no tasks yet")
        return

    for i,t in enumerate(tasks,1):
     status = "✔️" if t["done"] else "❌"
     print(f"{i}.{t['task']} [{status}]")

