from sys import stdin

def part_of_word(char):
    code = ord(char)
    return code >= ord('0') and code <= ord('9') or \
           code >= ord('a') and code <= ord('z') or \
           code >= ord('A') and code <= ord('Z') or \
           code == ord('_')
def is_digit(char):
    code = ord(char)
    return code >= ord('0') and code <= ord('9')

n, C, D = input().split()
if C == "yes":
    register_sence = True
else:
    register_sence = False
if D == "yes":
    start_digit = True
else:
    start_digit = False
keywords = set()
for _ in range(int(n)):
    word = input()
    if not register_sence:
        word = word.lower()
    keywords.add(word)


word_freq = dict()
word_appearance = dict()
word = ''
for i, c in enumerate(stdin.read()):
    if part_of_word(c):
        word += c
    elif len(word) > 0:
        if not register_sence:
            word = word.lower()
        if word not in keywords:
            if not ((len(word) == 1 or not start_digit) and is_digit(word[0])):
                word_freq[word] = word_freq.get(word, 0) + 1
                if word not in word_appearance:
                    word_appearance[word] = i
        word = ''

max_freq = max(word_freq.values())
most_freq_words = set()
for word in word_freq:
    if word_freq[word] == max_freq:
        most_freq_words.add(word)
first_freq_word = most_freq_words.pop()
first_freq_word_i = word_appearance[first_freq_word]
for word in most_freq_words:
    if word_appearance[word] < first_freq_word_i:
        first_freq_word = word
        first_freq_word_i = word_appearance[word]

print(first_freq_word)
        