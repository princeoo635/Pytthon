# 5. Count the frequency of each character in a string.
word=input("enter your word: ")
freq= {}
for c in word:
    if c in freq:
        freq[c]=freq[c] +1
    else:    
        freq[c]=1
print(freq)
