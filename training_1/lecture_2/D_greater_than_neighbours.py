def greater_neighbours(numbers):
    cnt = 0
    for i in range(1, len(numbers)-1):
        if numbers[i] > numbers[i-1] and numbers[i] > numbers[i+1]:
            cnt += 1
    return cnt


numbers = list(map(int, input().split()))
print(greater_neighbours(numbers))
