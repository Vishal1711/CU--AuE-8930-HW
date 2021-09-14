word = input()
word = word.split()

for i in word:
    if word.count(i) > 1:
        word.remove(i)

word.sort()
print(" ".join(word))
