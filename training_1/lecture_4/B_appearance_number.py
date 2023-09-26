from sys import stdin
words = stdin.read().split()
freq_dict = {}
ans = []
for word in words:
    ans.append(freq_dict.get(word, 0))
    freq_dict[word] = freq_dict.get(word, 0) + 1

print(*ans)
