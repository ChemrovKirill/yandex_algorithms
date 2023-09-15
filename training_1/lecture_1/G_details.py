N, K, M = map(int, input().split())

c_d = 0
if M <= K:
    while N >= K:
        c_nk = N // K
        R1 = N % K
        c_km = K // M
        R2 = c_nk * (K % M)
        c_d += c_nk * c_km
        N = R1 + R2
print(c_d)