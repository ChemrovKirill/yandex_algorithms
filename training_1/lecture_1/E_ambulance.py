def fast(K1, M, K2, P2, N2):
    if N2 > M:
        P1 = -1
        N1 = -1
    elif P2 == 1 and N2 == 1:
        if K1 <= K2:
            P1 = 1
            N1 = 1
        elif K1 < M:
            P1 = 1
            N1 = 0
        elif (K2//M + int(K2%M>0))*M >= K1:
            P1 = 1
            N1 = 0
        else:
            P1 = 0
            N1 = 0
    else:
        # fpf: number of flats per floor
        # leq_fpf <= fpf < g_fpf
        leq_fpf = K2 / (M * (P2 - 1) + N2)
        g_fpf = K2 / (M * (P2 - 1) + N2 - 1)
        if leq_fpf > int(leq_fpf):
            leq_fpf = int(leq_fpf) + 1
        else:
            leq_fpf = int(leq_fpf)
        if g_fpf > int(g_fpf):
            g_fpf = int(g_fpf)
        else:
            g_fpf = int(g_fpf) - 1
        if leq_fpf > g_fpf:  # contradiction
            P1 = -1
            N1 = -1
        else:
            P1_set = set()
            N1_set = set()
            for fpf in range(leq_fpf, g_fpf + 1):
                if K1 % fpf > 0:
                    P1_set.add((K1 // fpf) // M + 1)
                    N1_set.add((K1 // fpf) % M + 1)
                else:
                    if (K1 // fpf) % M != 0:
                        P1_set.add((K1 // fpf) // M + 1)
                        N1_set.add((K1 // fpf) % M)
                    else:
                        P1_set.add((K1 // fpf) // M + int((K1 // fpf) % M > 0))
                        N1_set.add(M)
            if len(P1_set) > 1:
                P1 = 0
            else:
                P1 = P1_set.pop()
            if len(N1_set) > 1:
                N1 = 0
            else:
                N1 = N1_set.pop()
    if N1 == 0 and M == 1:
        N1 = 1
    return P1, N1

K1, M, K2, P2, N2 = map(int, input().split())
print(*fast(K1, M, K2, P2, N2))

# stress test
"""
# Algorithm by Alexander Tereshin
# https://github.com/alexander-tereshin/yandex-algorithm-trainings_1.0 
import math, random
def slow(k1, m, k2, p2, n2):
    if k1 != k2:
        # list with all possible options of number of flats per floor
        ls = []
        for i in range(1, 1001):
            if math.ceil(math.ceil(k2 / i) / m) == p2 and math.ceil((k2 - (i * m) * (p2 - 1)) / i) == n2:
                ls.append(i)
        if len(ls) == 0:
            return -1, -1
        elif len(ls) == 1:
            x = ls[0]
            p1 = math.ceil(math.ceil(k1 / x) / m)
            n1 = math.ceil((k1 - (x * m) * (p1 - 1)) / x)
            return p1, n1
        else:
            p1_vals = set()
            n1_vals = set()
            for i in ls:
                p1 = math.ceil(math.ceil(k1 / i) / m)
                n1 = math.ceil((k1 - (i * m) * (p1 - 1)) / i)
                p1_vals.add(p1)
                n1_vals.add(n1)
            if len(p1_vals) > 1 and len(n1_vals) > 1:
                return 0, 0
            elif len(p1_vals) == 1 and len(n1_vals) > 1:
                return *p1_vals, 0
            elif len(p1_vals) > 1 and len(n1_vals) == 1:
                return 0, *n1_vals
            else:
                return *p1_vals, *n1_vals
    else:
        ls = []
        for i in range(1, 1001):
            if math.ceil(math.ceil(k2 / i) / m) == p2 and math.ceil((k2 - (i * m) * (p2 - 1)) / i) == n2:
                ls.append(i)
        if len(ls) == 0:
            return -1, -1
        else:
            return p2, n2


while True:
    randvals = []
    for i in range(5):
        randvals.append(random.randint(1, 100))
    K1, M, K2, P2, N2 = randvals
    slowans = slow(K1, M, K2, P2, N2)
    fastans = fast(K1, M, K2, P2, N2)
    print(*randvals)
    if slowans == fastans:
        print("OK")
    else:
        print("WA", fastans, slowans)
        break
"""
# special tests
"""
# fastans = fast(10, 14, 26, 2, 12) # (1, 10)
# fastans = fast(20, 14, 26, 2, 12) # (2, 6)
# fastans = fast(97, 64, 43, 1, 1) # (1, 0) - slow mistake
# fastans = fast(78, 16, 65, 1, 1) # (1, 0)
# fastans = fast(56, 7, 44, 1, 1) # (1, 0)  - slow mistake
"""

# time comparison
"""
from time import time
t1 = time()
random.seed(1)
for _ in range(1000):
    randvals = []
    for i in range(5):
        randvals.append(random.randint(1, 1000))
    K1, M, K2, P2, N2 = randvals
    slowans = slow(K1, M, K2, P2, N2)
    #fastans = fast(K1, M, K2, P2, N2)
t2 = time()
print(t2-t1)
"""