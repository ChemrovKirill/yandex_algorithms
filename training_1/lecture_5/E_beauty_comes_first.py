N, K = map(int, input().split())
trees = list(map(int, input().split()))
tree_set = set(trees)

left = 0
right = -1
best_left = 0
best_right = len(trees) - 1 
min_num = len(trees)
window_dict = dict()
while right < len(trees):
    if len(tree_set) > len(window_dict):
        right += 1
        if right >= len(trees):
            break
        window_dict[trees[right]] = window_dict.get(trees[right], 0) + 1
    else:
        if right - left + 1 < min_num:
            min_num = right - left + 1
            best_left = left
            best_right = right
        window_dict[trees[left]] -= 1
        if window_dict[trees[left]] == 0:
            window_dict.pop(trees[left])
        left += 1

print(best_left + 1, best_right + 1)
