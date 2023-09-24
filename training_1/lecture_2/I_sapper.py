def neighbours(m, field):
    ns = [[m[0]-1, m[1]-1], [m[0]-1, m[1]  ],
          [m[0]-1, m[1]+1], [m[0]  , m[1]-1], 
          [m[0]  , m[1]+1], [m[0]+1, m[1]-1],
          [m[0]+1, m[1]  ], [m[0]+1, m[1]+1],]
    real_ns = []
    for n in ns:
        if n[0] < 0 or n[1] < 0 or n[0] >= len(field) or \
                n[1] >= len(field[0]) or field[n[0]][n[1]] == '*':
            continue
        real_ns.append(n)
    return real_ns


def make_field(N, M, mines):
    field = [[0] * M for i in range(N)]
    for m in mines:
        field[m[0]][m[1]] = '*'
    for m in mines:
        for n in neighbours(m, field):
            field[n[0]][n[1]] += 1
    return field


N, M, K = map(int, input().split())
mines = []
for ik in range(K):
    mine = list(map(int, input().split()))
    mines.append([mine[0] - 1, mine[1] - 1])


field = make_field(N, M, mines)
for line in field:
    print(*line)
