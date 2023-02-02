emp={"name":"komal","age":28,"salary":25000,"company":"INFOTECH"}
print(type(emp))
print(emp)
print("enter the detials of new employee:")
emp["name"]=input("name:")
emp["age"]=int(input("age:"))
emp["salary"]=int(input("salary:"))
emp["company"]=input("company:")
print("printing the new data ",emp)