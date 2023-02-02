#if number of argument is unknown,add a * before the parameter
def my_function(*kids):
    print("the youngest child is "+kids[2])

my_function("anu","samu","urvi")
