l=[x for x in range(4)]
print(l)

d1={var:var+3 for var in l}
print(d1)

l1=[x for x in range(7)]
l2=["sun","mon","tue","wed","thur","fri","sat"]
print(l1)
print(l2)
d2={k:v for(k,v) in zip(l1,l2)}
print(d2)