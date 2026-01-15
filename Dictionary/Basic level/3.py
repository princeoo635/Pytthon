# 3. Access the value of a key given by the user.
info={'id': 1, 'name': 'Prince', 'age': 24, 'city': 'hyderabad'}
key=input("enter the key:")
if key in info:
    print(info[key])
else:
    print("key not found")