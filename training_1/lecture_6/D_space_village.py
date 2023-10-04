n, a, b, w, h = map(int, input().split())

def rbinsearch(L, R, check):
    while L < R:
        M = (L + R + 1) // 2
        if check(M):
            L = M
        else:
            R = M - 1
    return L

def check(d):
    block_a = a + 2*d
    block_b = b + 2*d
    if (w // block_a) * (h // block_b) >= n or \
        (w // block_b) * (h // block_a) >= n:
        return True

print(rbinsearch(0, min(w, h), check))
