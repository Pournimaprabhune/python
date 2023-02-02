#how to get the type code of an array
from array import *
array_num=array('i',[1,2,3,4,7,9,3,3,3])
print(array_num.typecode)
print(array_num.itemsize)
array_num.append(100)
print(array_num)
print(array_num.buffer_info())
print(array_num.count(3))
print("original array:",(array_num))
array_num.extend(array_num)
print("extented array :",(array_num))




