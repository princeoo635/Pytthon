# 3. Check whether a string is a palindrome.
s="abce"
rev=s[::-1]
if s==rev:
    print("palindrome")
else:
    print("not palindrome")