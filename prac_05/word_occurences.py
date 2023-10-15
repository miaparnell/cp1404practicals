"""
Word Occurrences
Estimate: 35 minutes
Actual: 30 minutes
"""

word_to_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
words = list(word_to_count.keys())
words.sort()

longest_word = max(len(word) for word in words)
for word in words:
    print(f"{word:{longest_word}} : {word_to_count[word]}")

