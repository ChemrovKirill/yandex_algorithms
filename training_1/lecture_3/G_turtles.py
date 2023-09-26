N = int(input())
a_set = set()
for _ in range(N):
    a, b = map(int, input().split())
    if a + b == N - 1 and a >= 0 and b >= 0:
        a_set.add(a)
print(len(a_set))
