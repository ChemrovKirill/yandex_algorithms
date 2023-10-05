N, K = map(int, input().split())
L_list = []
for _ in range(N):
    L_list.append(int(input()))

def rbinsearch(L, R, check):
    while L < R:
        M = (L + R + 1) // 2
        if check(M):
            L = M
        else:
            R = M - 1
    return L

def check(length):
    number = 0
    for L_i in L_list:
        number += L_i // length
    if  number >= K:
        return True
    
print(rbinsearch(0, max(L_list), check))
