print("\n using update method\n")
months=set(["january","february","march","april","may","june"])
print("\n printing original set:",months)
print("\n updating the original set\n")
months.update(["september","octobar","december"])
print("new set ",months)
for i in months:

    print(i)

print("\n remove item from set using discard and remove function \n" )

months.discard("may")
months.remove("june")
print("new set1:",months)

print("\nclear set\n")
months.clear()
print("new set 2:",months)

