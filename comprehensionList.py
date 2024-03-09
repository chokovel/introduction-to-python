sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
    if word != "quick":
        word_lengths.append(len(word))

print(words)
print(word_lengths)

numbers = [number*number for number in range(1,6)]
print(numbers)