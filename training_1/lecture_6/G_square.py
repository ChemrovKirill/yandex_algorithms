n = int(input())
m = int(input())
t = int(input())

def rbinsearch(L, R, check):
    while L < R:
        M = (L + R + 1) // 2
        if check(M):
            L = M
        else:
            R = M - 1
    return L

def check(w):
    if n * m - (n - 2*w) * (m - 2*w) <= t:
        return True
    
print(rbinsearch(0, min(n, m)//2, check))
