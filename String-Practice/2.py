# 2. Reverse a given string without using built-in reverse functions.

s="Python Program"
# print(s[::-1])
res=""
for c in s:
    res=c+res
print("reverse:",res)