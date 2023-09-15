def check(a, b, c, d, e):
    for x, y in [(a, b), (b, a),
                 (b, c), (c, b),
                 (c, a), (a, c),]:
        if e >= x and d >= y:
            return "YES"
    return "NO"

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

print(check(a, b, c, d, e))