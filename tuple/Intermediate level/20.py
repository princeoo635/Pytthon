# 20. Check if a tuple is a palindrome.
num = (1,2,3,2,1)
rev = tuple(reversed(num))
if num==rev:
    print ("palindrome")
else:
    print("not palindrome")
