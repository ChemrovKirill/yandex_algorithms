def is_monotonic(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] <= numbers[i-1]:
            return "NO"
    return "YES"


numbers = list(map(int, input().split()))
print(is_monotonic(numbers))