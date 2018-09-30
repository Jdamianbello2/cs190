words = []

while len(words) < 5:
    words.append(input("Enter a word: "))

print(words)

print(sorted(words))

words.reverse()

print(words)

words.sort(reverse=True)

print(words)

length = 0
longest = 0

for word in words:
    if len(word) > length:
        longest = word
        length = len(word)
print(longest)

