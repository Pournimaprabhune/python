def simple():
    for i in range(10):
            if(i%2==0):
               yield i  

#function call using for loop 
for i in simple():
        print(i)

print("\n multiple yeild \n" )

def abc():
    str1="first string"
    yield str1
    
    str2="second string"
    yield str2

    str3="third string"
    yield str3

b=abc()
print(next(b))
print(next(b))
print(next(b))
