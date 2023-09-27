N = int(input())
width2height = {}

for _ in range(N):
    w, h = map(int, input().split())
    if width2height.get(w, 0) < h:
        width2height[w] = h

total_height = sum(width2height.values())
print(total_height)
