# recursion example
def tri(k):
    if(k>0):
        result=k+tri(k-1)
    else:
        result=0

    return result

print("results =") 

print(tri(6))   


