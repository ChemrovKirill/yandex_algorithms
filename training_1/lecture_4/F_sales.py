from sys import stdin

name2goods = dict()
for line in stdin:
    name, good, amount = line.split()
    if name not in name2goods:
        name2goods[name] = dict()
    name2goods[name][good] = name2goods[name].get(good, 0) + int(amount)

for name in sorted(name2goods):
    print(f"{name}:")
    for good in sorted(name2goods[name]):
        print(good, name2goods[name][good])
