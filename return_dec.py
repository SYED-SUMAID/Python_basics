def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
              func(a)
        return wrapper 
    return decorator
@repeat(1)
def greet(a):
    print(f"Hello! {a}")
    #  chat = input("Are you the goat? (yes or no):").lower()
    #  if chat == "yes":
    #       print(f"Hey {a}")
    #  else:
    #     print("hi pussy")
 
greet("Billy")
