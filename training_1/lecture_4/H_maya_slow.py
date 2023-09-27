def word2dict(word):
    w_dict = dict()
    for char in word:
        w_dict[char] = w_dict.get(char, 0) + 1
    return w_dict


def words_in_seq(W, S):
    number_of_words = 0
    w_dict = word2dict(W)
    w_len = len(W)
    window = word2dict(S[:w_len])
    i = w_len
    while i <= len(S):
        if w_dict == window:
            number_of_words += 1
        if i < len(S):
            next_char = S[i]
            window[next_char] = window.get(next_char, 0) + 1
            char_to_del = S[i-w_len]
            window[char_to_del] -= 1
            if window[char_to_del] == 0:
                window.pop(char_to_del)
        i += 1
    return number_of_words


g, S_len = map(int, input().split())
W = input()
S = input()
print(words_in_seq(W, S))
