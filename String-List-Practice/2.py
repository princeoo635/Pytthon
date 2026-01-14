# 2. Find the word with maximum length in a sentence.
sentence=input("enter your text: ")
print(max(sentence.split(),key=len))