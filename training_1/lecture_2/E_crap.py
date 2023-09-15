def find_vasily(dists):
    vas_dist = -1
    win_dist = max(dists)
    winner_is_found = False
    for i in range(1, len(dists)-1):
        if dists[i-1] == win_dist:
            winner_is_found = True
        if winner_is_found == False:
            continue
        if dists[i] % 10 != 5:
            continue
        if dists[i] <= dists[i+1]:
            continue
        if dists[i] > vas_dist:
            vas_dist = dists[i]
    if vas_dist == -1:
        return 0
    cnt = 1
    for i in range(len(dists)):
        if vas_dist < dists[i]:
            cnt += 1
    return cnt

n = int(input())
dists = list(map(int, input().split()))
print(find_vasily(dists))
