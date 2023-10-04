w, h, n = map(int, input().split())

def lbinsearch(L, R, check):
    while L < R:
        M = (L + R) // 2
        if check(M):
            R = M
        else:
            L = M + 1
    return L

def check(size):
    if (size // w) * (size // h) >= n:
        return True
    
print(lbinsearch(0, max(w,h)*n, check))
