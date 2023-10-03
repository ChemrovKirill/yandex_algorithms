n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x,y))

cnt = 0
for i in range(n):
    used_vectors = set()
    neighbors = []
    for j in range(n):
        vector_x = points[i][0] - points[j][0]
        vector_y = points[i][1] - points[j][1]
        vector_len2 = vector_x**2 + vector_y**2
        neighbors.append(vector_len2)
        if (vector_x, vector_y) in used_vectors:
            cnt -= 1
        used_vectors.add((-vector_x, -vector_y))
    neighbors.sort()
    R = 0
    for L in range(len(neighbors)):
        while R < len(neighbors) and neighbors[R] == neighbors[L]:
            R += 1
        cnt += R - L - 1

print(cnt)
