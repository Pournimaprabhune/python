empty_tuple=0
print("empty tuple:",empty_tuple)

int_tuple=(1,2,34,5)
print("integer tuple",int_tuple)

mixed_tuple=(4,"python,4.5")
print("mixed tuple:",mixed_tuple)

nested_tuple=12,"python",{4:5,6:2,8:2},(5,3,5,6)
print("nested tuple :",nested_tuple)
print(type(nested_tuple))
try:
    nested_tuple[1] = 4.2
except:
        print(TypeError)   