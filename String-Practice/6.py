# 6. Remove all duplicate characters from a string.

string = input("enter your string: ")
dup = {}
for c in string:
    if c not in dup:
        dup[c] = 1
for ch in dup:
    print(ch, end="")

