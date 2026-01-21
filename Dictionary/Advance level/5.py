# 5. Create a dictionary of squares of numbers from 1 to n.
n=int(input("enter a number: "))
square_dict = { i : i*i for i in range(1,n+1)}
print(square_dict)