from re import X

def decore1(func):

    def inner():

        x=func()

        return x*x
    
    return inner

def decore(func):

    def inner():

        x=func
        
        return 2*X
    
    return inner
@decore1
@decore
def num() :
    return 10
print(num())     