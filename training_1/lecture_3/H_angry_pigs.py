N = int(input())
x_set = set()
for _ in range(N):
    x, _ = map(int, input().split())
    x_set.add(x)
print(len(x_set))
