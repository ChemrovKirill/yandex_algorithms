N, M = map(int, input().split())
set_a = set()
for _ in range(N):
    set_a.add(int(input()))
set_b = set()
for _ in range(M):
    set_b.add(int(input()))

set_intersect = set_a & set_b
set_a_remain = set_a - set_intersect
set_b_remain = set_b - set_intersect
print(len(set_intersect))
print(*sorted(set_intersect))
print(len(set_a_remain))
print(*sorted(set_a_remain))
print(len(set_b_remain))
print(*sorted(set_b_remain))
