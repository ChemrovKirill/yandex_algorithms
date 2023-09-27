def update_dict(word):
    w_dict = dict()
    for char in word:
        w_dict[char] = w_dict.get(char, 0) + 1
    return w_dict


from string import ascii_uppercase, ascii_lowercase


def words_in_seq(W, S):
    number_of_words = 0
    w_dict = dict()
    window = dict()
    for c in ascii_lowercase + ascii_uppercase:
        w_dict[c] = 0
        window[c] = 0
    for char in W:
        w_dict[char] += 1
    w_len = len(W)
    for char in S[:w_len]:
        window[char] += 1
    i = w_len
    while i <= len(S):
        if w_dict == window:
            number_of_words += 1
        if i < len(S):
            next_char = S[i]
            window[next_char] += 1
            char_to_del = S[i-w_len]
            window[char_to_del] -= 1
        i += 1
    return number_of_words


g, S_len = map(int, input().split())
W = input()
S = input()
print(words_in_seq(W, S))
