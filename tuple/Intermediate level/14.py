# 14. Slice a tuple to get middle elements.
num = (1,2,3,4,5,6,8,9,4,2,3,4)
n = len(num)
middle_elements = num[(n-1)//2 : (n//2)+1]
print(middle_elements)
