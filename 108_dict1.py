emp={"name":"komal","age":28,"salary":25000,"company":"INFOTECH"}
print(type(emp))
print(emp)
print("printing employee data")
print("name=%s"%emp["name"])
print("age=%d"%emp["age"])
print("salary=%d"%emp["salary"])
print("company=%s"%emp["company"])


print("\n deleting some of emp data")
del emp["name"]
del emp["company"]
print("new dictionary:",emp)

print("\n delete dictionary")
del emp
print(emp)




