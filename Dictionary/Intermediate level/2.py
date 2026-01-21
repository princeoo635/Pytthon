# 2. Count the frequency of each word in a sentence.
sentence="this is a lovely day how are you today lw go fro a walk"
word=sentence.split()
freq={}
for i in word:
    freq[i]=freq.get(i,0)+1
print(freq)