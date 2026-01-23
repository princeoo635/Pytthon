# 19. Find the second largest element in a tuple.
num = (1,2,3,4,5,6,8,9,4,2,3)
unique = tuple(set(num))
unique_sorted = sorted(unique)
print(unique_sorted[-2])
