print("\n generator without using yeild keyword")
list=[1,2,3,4,5,6,7]
print("\n list comprehension \n")
a1=[x**3 for x in list]
print(a1)

print(" \n generator expression \n")
a=(x**3 for x in list)#it gives error 
print(a)