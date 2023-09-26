def extend(rect, r):
    xpy_min, xpy_max, xmy_min, xmy_max = rect
    xpy_min -= r
    xpy_max += r
    xmy_min -= r
    xmy_max += r
    return xpy_min, xpy_max, xmy_min, xmy_max

def intersect(rect_1, rect_2):
    ans_0 = max(rect_1[0], rect_2[0])
    ans_1 = min(rect_1[1], rect_2[1])
    ans_2 = max(rect_1[2], rect_2[2])
    ans_3 = min(rect_1[3], rect_2[3])
    return (ans_0, ans_1, ans_2, ans_3)


t, d, n = map(int, input().split())
pos_rect = (0, 0, 0, 0)
for _ in range(n):
    pos_rect = extend(pos_rect, t)
    nav_x, nav_y = map(int, input().split())
    nav_rect = extend((nav_x + nav_y, nav_x + nav_y, nav_x - nav_y, nav_x - nav_y), d)
    pos_rect = intersect(pos_rect, nav_rect)

final_poses = []
for xpy in range(pos_rect[0], pos_rect[1] + 1):
    for xmy in  range(pos_rect[2], pos_rect[3] + 1):
        double_x = xpy + xmy
        if double_x % 2 == 0:
            x = double_x // 2
            y = xpy - x
            final_poses.append((x, y))
    
print(len(final_poses))
for pos in final_poses:
    print(*pos)