# 4. Find the first non-repeating character in a string.

s=input("enter text:")
for c in s:
    if s.count(c)==1:
        print(f"{c} is non repeating character")
        break
else:
    print("no non repeating character")