def nearest_number(numbers, x):
    nearest = numbers[0]
    diff = abs(x - nearest)
    for i in range(1, len(numbers)):
        cur_diff = abs(x - numbers[i])
        if cur_diff < diff:
            nearest = numbers[i]
            diff = cur_diff
    return nearest


N = int(input())
numbers = list(map(int, input().split()))
x = int(input())

print(nearest_number(numbers, x))
