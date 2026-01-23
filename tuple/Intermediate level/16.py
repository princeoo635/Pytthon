# 16. Convert a tuple of tuples into a dictionary.
num=((1,2),(3,4),(5,6))
nums={}
for i in range(len(num)):
    nums[num[i][0]]=num[i][1]
print(nums)