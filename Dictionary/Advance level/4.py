# 4. Group words with the same length using a dictionary.
words = ["apple", "bat", "cat", "banana", "dog", "ant"]
grouped={}
for val in words:
    length=len(val)
    if length not in grouped:
        grouped[length]=[]
    grouped[length].append(val)
print(grouped)