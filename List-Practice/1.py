# 1. Find the largest and smallest elements in a list.
lst = list(map(int, input("Enter numbers: ").split()))

largest = lst[0]
smallest = lst[0]

for n in lst:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n

print("Largest:", largest)
print("Smallest:", smallest)
