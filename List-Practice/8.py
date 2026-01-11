# 8. Rotate a list to the right by k positions.
values=[1,2,3,4,5]
n=int(input("enter position to shift by: "))
for i in range(n):
    values.insert(0,values.pop())
print(values)