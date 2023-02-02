list=[1,2,2,3,2,5,7,6,8,5]
list1=[]
print("after deleting duplicate elment in list")
for i in list:

    if i  not in list1:
                
                  list1.append(i)

print(list1)

print("\n to find the sum of element in list \n" )
sum=0
for i in list:
            sum=sum+i
print("the sum is",sum)

print("find common element in list \n")
l1=[1,2,3,4,5,6]
l2=[7,8,9,10,2,4]
for x in l1:
         for y in l2:
                 if x==y:
                       print("common element:",x)        