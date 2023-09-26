n = int(input())
limits = list(map(int, input().split()))
k = int(input())
presses = list(map(int, input().split()))

for press in presses:
    limits[press-1] -= 1

for limit in limits:
    if limit < 0:
        print("YES")
    else:
        print("NO")
