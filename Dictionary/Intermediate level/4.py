# 4. Sort a dictionary by its values.
num_dict={'a':1,'b':2,'c':3,'d':8,'e':4}
sorted_dict = dict(sorted(num_dict.items(), key=lambda x: x[1]))
print(sorted_dict)

