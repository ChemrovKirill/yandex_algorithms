N = int(input())
shirts = list(map(int, input().split()))
M = int(input())
pants = list(map(int, input().split()))

min_diff = abs(pants[0] - shirts[0])
best_shirt = shirts[0]
best_pants = pants[0]
p = 0
s = 0
while p < len(pants) and s < len(shirts):
    diff = abs(pants[p] - shirts[s])
    if diff < min_diff:
        min_diff = diff
        best_shirt = shirts[s]
        best_pants = pants[p]
    if pants[p] < shirts[s]:
        p += 1
    elif pants[p] > shirts[s]:
        s += 1
    else:
        break

print(best_shirt, best_pants)
