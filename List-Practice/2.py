# 2. Remove duplicate elements from a list.

values=[1,3,9,3,5,5,6,7]
dup={}
for val in values:
    if val not in dup:
        dup[val]=1
result=list(dup.keys())
print(result)
