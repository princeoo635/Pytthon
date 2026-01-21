# 8. Remove keys with None values.
data = {
    "name": "Prince",
    "age": None,
    "city": "Hyderabad",
    "email": None
}
new_data={}
for k,v in data.items():
    if v != None:
        new_data[k]=v
print(new_data)