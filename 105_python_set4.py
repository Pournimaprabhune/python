print("\n using union  and intersection operater")
days1=set(["monday","tuesday","wednesday","thursay","friday","saturday","sunday"])
days2=set(["friday","saturday","sunday"])
print("union set:",days1|days2)
print("intersection set:",days1&days2)

print("\n union and intersection method")
a={1,2,3,4,5,6,7,8,9,10}
b={2,3,4,5,6}
print("union set:",a.union(b))
print("inetersection set:",a.intersection(b))


#set1=a.intersection(b)
#print(set1)

s1={"komal","pournima","shaila"}
s2={"priyanka","shaila"}
s3={"akshta","shaila"}
s1.intersection_update(s2,s3)
print(s1)

print("using subtraction operator:",days1-days2)
print("using difference method:",days1.difference(days2))


