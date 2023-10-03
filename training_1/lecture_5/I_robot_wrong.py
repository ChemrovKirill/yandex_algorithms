K = int(input())
string = input()

L = 0
R = -1
window_dict = dict()
cnt = 0
while R < len(string) - 1 or L < R:
    if len(window_dict) <= K and R < len(string) - 1:
        R += 1
        window_dict[string[R]] = window_dict.get(string[R], 0) + 1
    else:
        window_dict[string[L]] -= 1
        if window_dict[string[L]] == 0:
            window_dict.pop(string[L])
        L += 1
    if R - L + 1 > K and len(window_dict) <= K:
        cnt += 1

print(cnt)
