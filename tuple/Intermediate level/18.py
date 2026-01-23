# 18. Remove an element from a tuple.
num = (1,2,3,4,5,6,8,9,4,2,3)
new_num=list(num)
new_num.pop(9)
print(tuple(new_num))