n = int(input())
pairs = []  # the second frequancy is closer than the first one
f1 = float(input())
for _ in range(n-1):
    f2, ans = input().split()
    f2 = float(f2)
    if ans == 'closer':
        pairs.append((f1, f2))
    elif ans == 'further':
        pairs.append((f2, f1))
    f1 = f2


def find_bounds(pairs):
    left = 30.
    right = 4000.
    for f1, f2 in pairs:
        new_bound = (f1 + f2) / 2
        if f1 == f2:
            continue
        elif f1 < f2:
            if new_bound > left:
                left = new_bound
        else:
            if new_bound < right:
                right = new_bound
    return (left, right)

print(*find_bounds(pairs))