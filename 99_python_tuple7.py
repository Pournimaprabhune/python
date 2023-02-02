print("changing tuple")
tuple1="python","tuple","ordered","immutable",[1,2,3,4]
try:
    tuple1[2]="items"
    print(tuple1)
except Exception as e:
    print(e)

tuple1[-1][2]=10
print(tuple1)

tuple1=("python","items")
print(tuple1)
