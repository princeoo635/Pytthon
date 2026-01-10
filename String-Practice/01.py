# Count the number of vowels in a string.
word=input("Enter your text : ")
# word="i am strong person"
c=0
for letter in word:
    if letter in "AEIOUaeiou":
        c=c+1
print(c)