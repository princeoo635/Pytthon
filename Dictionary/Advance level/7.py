# 7. Use defaultdict to count elements.
from collections import defaultdict

word = "apple"
freq = defaultdict(int)

for ch in word:
    freq[ch] += 1

print(freq)
