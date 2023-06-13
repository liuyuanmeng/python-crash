
def say_hi():
    print("STILL THERE?")
say = hello(say_hi)
print(say)
@decorator
# Higher Order Function HOC
def hello(func):
    func()

# Decorator 
def my_decorator(func):
    def wrap_func():
        func()
    return wrap_func
