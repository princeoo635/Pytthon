# 9. Convert a list of tuples into a dictionary.
key=('a','e','s','d','f','g')
val=(1,2,3,4,5,6)
num_dict={}
for k,v in zip(key,val):
    num_dict[k] = v
print(num_dict)