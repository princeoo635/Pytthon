# 3.  Count how many times each word appears in a sentence.
sentence=input("Enter the text: ")
words=sentence.split()
unique_word=set()
for w in words:
    if w not in unique_word:
        unique_word.add(w)
        print(w,"=",words.count(w))