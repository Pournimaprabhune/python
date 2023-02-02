a="hello,world!"
print(a[1])
print(len(a))
print(a[2:5])
print(a[:5])
print(a.split(","))

b="   hello ,python!  "
print(b.strip())#remove whitspaces
print(b.replace("python","pournima"))
c=a+b
print(c)
d=a+" "+b
print(d)
for x in "banana":
    print(x)