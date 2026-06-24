import threading
import time

def worker (num):
    print(f"thread {num}: starting")
    time.sleep(6)
    print(f"thread {num}: ending")

threads = []
for i in range (7):
    thread = threading.Thread(target = worker,args =(i,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
print("All threads completed")    
# import threading
# import time

# def task(name):
#     print(f"Task {name} started")
#     time.sleep(2)
#     print(f"Task {name} finished")

# t1 = threading.Thread(target=task, args=("A",))
# t2 = threading.Thread(target=task, args=("B",))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("All tasks completed")
