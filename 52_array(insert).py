from array import *
nums=array("i",[1,2,4,5,6,7])
nums.insert(2,3)#(i,x)
print(nums)
print(nums.pop(4))
print(nums)
nums.reverse()
print(nums)
nums.remove(4)
print(nums)
for x in nums:
    print(x)