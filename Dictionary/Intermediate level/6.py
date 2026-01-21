# 6. Remove duplicate values from a dictionary.
num_dict={'a':1,'b':2,'c':3,'d':8,'e':4,'f':3}
val=[]
dupval=[]
for k , v in num_dict.items():
    if v not in val:
        val.append(v)
    else:
        dupval.append(k)

for i in dupval:
    num_dict.pop(i)
print(num_dict)