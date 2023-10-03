K = int(input())
string = input()

prevlen = 0
cnt = 0
for i in range(K, len(string)):
    if string[i] == string[i - K]:
        prevlen += 1
        cnt += prevlen
    else:
        prevlen = 0

print(cnt)
