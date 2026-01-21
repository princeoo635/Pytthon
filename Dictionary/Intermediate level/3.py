# 3. Find the key with the maximum value.
num_dict={'a':1,'b':2,'c':3,'d':8,'e':4}
maxvalue = max(num_dict.values())
for key, value in num_dict.items():
    if value==maxvalue:
        print(key)
        break

