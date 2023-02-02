print("show how to access tuple element")

tuple="python","tuple","ordered","collection"
print(tuple[0])
print(tuple[1])

try:
    print(tuple[5])

except Exception as e:
        
        print(e)   

try:
    print(tuple[1.0])

except Exception as e:
        
        print(e)   

tuple1="tuple",[4,6,2,4],(6,2,6,7)
  
print(tuple1[0][3])

print(tuple1[1][1])
