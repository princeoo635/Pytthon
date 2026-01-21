# 1. Count the frequency of each character in a string using a dictionary.
word="prinewlilsafkfdjasdf"
freq={}
for i in word:
    freq[i]=freq.get(i,0)+1
print(freq)