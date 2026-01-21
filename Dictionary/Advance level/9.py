# 9. Find duplicate values in a dictionary.
num_dict={'a':1,'b':2,'c':3,'d':8,'e':4,'f':3}
seen = set()
duplicates = set()

for v in num_dict.values():
    if v in seen:
        duplicates.add(v)
    else:
        seen.add(v)

print(duplicates)
