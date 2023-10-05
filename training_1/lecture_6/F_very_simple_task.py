N, x, y = map(int, input().split())

def lbinsearch(L, R, check):
    while L < R:
        M = (L + R) // 2
        if check(M):
            R = M
        else:
            L = M + 1
    return L

def check(time):
    if time // x + time // y >= N - 1: # 1 1st copy 
        return True

print(lbinsearch(0, (x + y) * N, check) + min(x, y))
