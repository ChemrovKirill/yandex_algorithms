def neighborhood(p, r):
    poses = set()
    for steps_num in range(r + 1):
        for xi in range(steps_num + 1):
            for yi in range(steps_num - xi + 1):
                new_poses = {(p[0] + xi, p[1] + yi), 
                             (p[0] + xi, p[1] - yi), 
                             (p[0] - xi, p[1] + yi), 
                             (p[0] - xi, p[1] - yi)}
                poses.update(new_poses)
    return poses


def manhatten_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


t, d, n = map(int, input().split())
cur_posposes = {(0,0)}  # init possible positions 
for _ in range(n):
    nav_pos = tuple(map(int, input().split()))
    new_posposes = set()
    for newpos in neighborhood(nav_pos, d):
        for curpos in cur_posposes:
            if manhatten_dist(curpos, newpos) <= t:
                new_posposes.add(newpos)
                break
    cur_posposes = new_posposes

print(len(cur_posposes))
for pos in cur_posposes:
    print(*pos)
