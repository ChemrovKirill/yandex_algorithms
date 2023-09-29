N = int(input())
points = list()
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

ascent_prefix = [0]
descent_prefix = [0]
for ip in range(0, len(points) - 1):
    diff = points[ip+1][1] - points[ip][1]
    if diff > 0:
        ascent_prefix.append(ascent_prefix[ip] + diff)
        descent_prefix.append(descent_prefix[ip])
    else:
        ascent_prefix.append(ascent_prefix[ip])
        descent_prefix.append(descent_prefix[ip] - diff)

M = int(input())
for _ in range(M):
    s, f = map(int, input().split())
    if s <= f:
        print(ascent_prefix[f-1] - ascent_prefix[s-1])
    else:
        print(descent_prefix[s-1] - descent_prefix[f-1])
