# 6. Convert a dictionary into a list of tuples.
num_dict={'a':1,'b':2,'c':3,'d':8,'e':4}
num=[]
for k,v in num_dict.items():
    num.append((k,v))
print(num)