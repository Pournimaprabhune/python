def hello(func):

    def inner1():

        print("hello this is before function execution")
        func()

        print("this is after function execution")

    return inner1

def function():

    print("this is inside function")

function=hello(function)

function()