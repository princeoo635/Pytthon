# 3. Reverse a list without using reverse() or slicing.

values=[3,5,8,0,3,5,7,8]
rev=[]
for v in values:
    rev.insert(0,v)
print(rev)
