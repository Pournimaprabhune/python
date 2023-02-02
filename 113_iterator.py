mytuple=("apple","banana","cherry")
a=iter(mytuple)
print(next(a))
print(next(a))
print(next(a))
for x in mytuple:
    print(x)

print("string are also iterable object,containing sequence of characater")
mystr="banana"
b=iter(mystr)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))