def decorator(func):
    def wrapper():
        print("Car starting in..")
        print("3")
        print("2")
        print("1")
        func()
    return wrapper
@decorator
def start_the_car():
     print("grrrrrrrrrrrrrrrrrrrrrrrrrrrrrr!")

S  = decorator(start_the_car)
S()
