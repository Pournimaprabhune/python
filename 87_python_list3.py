list=[1,2,3,4,5,6,7]
print(list[0])
print(list[1])
print(list[3])
print(list[0:6])
print(list[:])
print(list[2:5])


print("\nlist1 operation\n")
l1=[1,2,3,4,5]
print("\n negative index")
print(l1[-1])
print(l1[-3:])
print(l1[:-1])
print(l1[-3:-1])

print("\n updating list value\n")
print(list)
list[2]=10
print(list)
list[1:3]=[89,78]
print(list)
list[-1]=25
print(list)
print(list*2)
print(list+l1)
print(2 in l1)
print("lenth list:",len(list))
print("length l1:",len(l1))

for i in l1:
    print(i)

print("\nadding element to list\n")

l2=[]
n=int(input("enter the number of elements in the list: "))
for i in range(0,n) :
     l2.append(input("enter the item :"))
print("printing the list items")
print(l2)



