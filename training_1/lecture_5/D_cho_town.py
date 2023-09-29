n, r = map(int, input().split())
d_list = list(map(int, input().split()))

dr = 1
cnt = 0
for dl in range(len(d_list)):
    while dr < len(d_list):
        if d_list[dr] - d_list[dl] > r:
            cnt += len(d_list) - dr
            break
        else:
            dr += 1
print(cnt)
