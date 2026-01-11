# 10.  Find common elements between two lists.
val1=[2,5,7,8,9,44,33,77,55]
val2=[3,5,67,89,9,7,65,4,3,3]
val=[]
for v in val1:
    if v in val2:
        val.append(v)
print(val)
