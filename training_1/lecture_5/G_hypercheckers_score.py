n, k = map(int, input().split())
cards_init = list(map(int, input().split()))

cards2num = dict()
for c in cards_init:
    if cards2num.get(c, 0) < 3:
        cards2num[c] = cards2num.get(c, 0) + 1

cards = sorted(cards2num)
cnt = 0
l = 0
r = 0
r_start = 0
more_2_num = 0
for l in range(len(cards)):
    for r in range(r_start, len(cards) + 1):
        if r == len(cards) or cards[r] > k * cards[l]:
            r_start = r
            # 3 different
            cnt += 3 * (r - l - 1) * (r - l - 2)
            # 2 identical l
            if cards2num[cards[l]] >= 2:
                cnt += 3 * (r - l - 1)
                more_2_num -= 1
            # 3 identical l
            if cards2num[cards[l]] == 3:
                cnt += 1
            # 2 identical not l
            cnt += 3 * more_2_num
            break
        if cards2num[cards[r]] >= 2:
            more_2_num += 1
            
print(cnt)
