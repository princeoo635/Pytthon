# 8. Find the longest word in a sentence.

sentence=input("enter your sentence : ")
word=""
list=sentence.split()
for v in list:
    if len(v)>len(word):
        word=v
print(word)