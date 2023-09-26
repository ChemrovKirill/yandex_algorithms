from sys import stdin
words = stdin.read().split()
freq_dict = {}
for word in words:
    freq_dict[word] = freq_dict.get(word, 0) + 1
max_freq = max(freq_dict.values())
most_freq_words = []
for word in freq_dict:
    if freq_dict[word] == max_freq:
        most_freq_words.append(word)
print(min(most_freq_words))
