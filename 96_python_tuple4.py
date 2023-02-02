print("\n show how delete element in python tuple \n")

tuple="python","tuple","ordered","immutable","collection","object"

try:
    del tuple[3]
    print(tuple)
except Exception as e:
    print(e)   


del tuple
try:
   print(tuple)
except Exception as e:
    print(e)   

