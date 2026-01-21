# 3. Find the student with the highest marks.
student_details = {
    "one":{ "name":"prince", "marks":78 },
    "two":{ "name":"rahul", "marks":56 },
    "three":{ "name":"kabir", "marks":58 },
    "four":{ "name":"suresh", "marks":78 },
    "five":{ "name":"mohab", "marks":89 },
    "six":{ "name":"sam", "marks":78 }
}
max_marks=0
name=''
for i in student_details.values():
    if max_marks<=i["marks"]:
        max_marks=i["marks"]
        name=i["name"]
print(name)