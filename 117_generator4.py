def table():
    
    a=int(input("enter number:")) 
    for i in range(1,11):
             yield a*i
             i=i+1

for i in table():

           print(i)