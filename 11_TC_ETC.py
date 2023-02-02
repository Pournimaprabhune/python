print("explicite type coversion")
num_int=123
num_str="456"
print("datatype of num_int =",type(num_int))
print("datatype of num_str before typecasting =",type(num_str))
num_str=int(num_str)
print("datatype of num_str after typecasting =",type(num_str))
num_sum=num_int+num_str
print("the sum of num_int and num_str=",num_sum)
print("datatype of num_sum",type(num_sum))