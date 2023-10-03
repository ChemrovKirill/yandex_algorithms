n, k = map(int, input().split())
string = input()

char2num = dict()
l = 0
r = 0
max_len = 1
best_l = l
while r < len(string):
    char2num[string[r]] = char2num.get(string[r], 0) + 1
    while char2num[string[r]] > k:
        char2num[string[l]] -= 1
        l += 1
    if r - l + 1 > max_len:
        max_len = r - l + 1
        best_l = l
    r += 1

print(max_len, best_l + 1)
