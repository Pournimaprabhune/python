def hello(func):
    def inner1(*args,**kwargs):
        print("before execution")
        value=func(*args,**kwargs)
        print("after execution")
        return value
    return inner1
#@hello 
def sum(x,y):
    print("inside function")
    return x+y
x,y=1,2
sum=hello(sum)
print("sum=",sum(x,y))
