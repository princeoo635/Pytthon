# 5. Count even and odd numbers in a list.
values=[3,5,8,0,3,5,7,8]
even_count=0
odd_count=0
for i in values:
    if i%2==0:
        even_count +=1
    else:
        odd_count +=1
print("even:",even_count)
print("odd:",odd_count)
