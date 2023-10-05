N, R, C = map(int, input().split())
heights = []
for _ in range(N):
    heights.append(int(input()))

heights = sorted(heights)

def lbinsearch(L, R, check):
    while L < R:
        M = (L + R) // 2
        if check(M):
            R = M
        else:
            L = M + 1
    return L

def check(uncomf):
    groups_num = 0
    i = C-1
    while i < N:
        if heights[i] - heights[i-C+1] <= uncomf:
            groups_num += 1
            i += C
        else:
            i += 1
    if groups_num >= R:
        return True
if C == 1:
    print(0)
else:
    print(lbinsearch(0, heights[-1], check))
