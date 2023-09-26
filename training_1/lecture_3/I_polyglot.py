N = int(input())
set_all = set()
set_at_least_1 = set()
for i in range(N):
    M = int(input())
    set_cur = set()
    for _ in range(M):
        lang = input()
        set_cur.add(lang)
        set_at_least_1.add(lang)
    if i == 0:
        set_all = set_cur
    else:
        set_all = set_all & set_cur

print(len(set_all))
for lang in set_all:
    print(lang)
print(len(set_at_least_1))
for lang in set_at_least_1:
    print(lang)
