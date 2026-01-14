# 4. Remove empty strings from a list of strings.
sen_list = ["apple", "mango", "", "banana", "orange", ""]
sen_list = [s for s in sen_list if s != ""]
print(sen_list)
