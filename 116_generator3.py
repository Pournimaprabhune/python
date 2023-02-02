print("\n generator without using yeild keyword")
list=[1,2,3,4,5,6,7]

print(" \n generator expression \n")
a=(x**3 for x in list)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))