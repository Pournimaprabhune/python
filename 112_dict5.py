emp={"name":"komal","age":28,"salary":25000,"company":"INFOTECH"}
print(" print all the keys of dictionary")
for i in emp:
   print(i)

print("\n print all the values of dictionary")
#for x in emp:
    #print(emp[x])

for x in emp.values():
    print(x)

print("\n print the items of the dictionary by using item() method")
for x in emp.items():
    print(x)

for x,y in emp.items():
    print(x,y)


