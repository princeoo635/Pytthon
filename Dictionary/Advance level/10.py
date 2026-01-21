# 10. Count occurrences of elements in a list using a dictionary.
words = ["apple", "bat", "cat", "banana", "dog", "ant"]
fruits={}
for v in words:
    if v not in fruits:
        fruits[v]=1
    else:
        fruits[v] += 1
print(fruits)