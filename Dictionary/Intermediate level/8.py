# 8. Swap keys and values in a dictionary.
num_dict={'a':1,'b':2,'c':3,'d':8,'e':4,'f':3}
rev_num_dict = { v:k for k,v in num_dict.items()}
print(num_dict)
print(rev_num_dict)