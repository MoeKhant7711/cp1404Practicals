"""
CP1404/CP5632 Practical  
Word Occurrences Counter  

Estimate: 30 minutes  
Actual time: [Fill in your time here]  
"""

words_to_count = {}
lengths = []

text = input("Text: ")
words = text.split(" ")
for text in words:
    if text in words_to_count.keys():
        words_to_count[text] += 1
    else:
        words_to_count[text] = 1
listed_words = words_to_count.keys()
sorted_words = sorted(listed_words)
for words in words_to_count.keys():
    length = len(words)
    lengths.append(length)
    width = max(lengths)
for text in sorted_words:
    print(f"{text:<{width}}: {words_to_count[text]}")
