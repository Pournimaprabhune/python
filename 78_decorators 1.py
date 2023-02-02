#passing the function as an agrument
def shout(text):

    return text.upper()

def honda(text):

    return text.lower()

def greet(func):

        greeting=func("hii anushree")
        print(greeting)

greet(shout)

greet(honda)      