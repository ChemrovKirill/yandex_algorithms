a1, b1, a2, b2 = map(int, input().split())

s_best = (a1 + a2) * (b1 + b2)

for a, b in [(a1 + a2, max(b1, b2)),
             (a1 + b2, max(b1, a2)),
             (b1 + a2, max(a1, b2)),
             (b1 + b2, max(a1, a2)),]:
    s = a * b
    if s < s_best:
        s_best = s
        a_best, b_best = a, b

print(a_best, b_best)