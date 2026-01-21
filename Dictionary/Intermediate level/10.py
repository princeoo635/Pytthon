# 10. Find common keys between two dictionaries.
dict_one={'a':1,"v":"s","s":"e"}
num_dict={'a':1,'b':2,'c':3,'d':8,'e':4}
keyone=set(dict_one.keys())
keytwo=set(num_dict.keys())
print(keyone.intersection(keytwo))